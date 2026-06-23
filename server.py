"""
AGM Translation Tool — local inference with Hugging Face Transformers + sarvam-m
No API keys. No internet calls at runtime (after the one-time model download).

Run:
    python server.py

Then open http://localhost:5000
"""

import os
import json
import threading
import time
from flask import Flask, request, Response, send_from_directory
from prompts import build_translate_prompt, build_review_prompt

# ─────────────────────────────────────────────────────────────────────────────
# Config
# ─────────────────────────────────────────────────────────────────────────────
# MODEL_NAME = os.environ.get("SARVAM_MODEL", "sarvamai/sarvam-m")
MODEL_NAME = r"C:\Users\ASUS\sarvam-translate"
#QUANT_MODE = "cpu"
QUANT_MODE = "4bit"
# "4bit" -> ~14-16GB VRAM (recommended for most consumer GPUs, e.g. RTX 3090/4090)
# "8bit" -> ~26-28GB VRAM
# "none" -> full bf16, ~48GB VRAM (datacenter GPUs only)
# "cpu"  -> no GPU, runs on CPU only (slow, needs ~48GB system RAM)
# QUANT_MODE = os.environ.get("SARVAM_QUANT", "4bit")

MAX_NEW_TOKENS = int(os.environ.get("SARVAM_MAX_TOKENS", "1024"))
PORT = int(os.environ.get("PORT", "5000"))

app = Flask(__name__, static_folder="public")

# ─────────────────────────────────────────────────────────────────────────────
# Lazy model loading (loads once, on first request, in a background-safe way)
# ─────────────────────────────────────────────────────────────────────────────
_model = None
_tokenizer = None
_load_lock = threading.Lock()
_load_error = None
_load_status = "not_started"  # not_started -> loading -> ready -> error


def load_model():
    global _model, _tokenizer, _load_error, _load_status
    with _load_lock:
        if _model is not None or _load_status == "loading":
            return
        _load_status = "loading"
        try:
            import torch
            from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

            print(f"[sarvam] Loading tokenizer for {MODEL_NAME} ...")
            tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

            kwargs = {}
            if QUANT_MODE == "4bit":
                print("[sarvam] Loading model in 4-bit (bitsandbytes NF4) ...")
                bnb_config = BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_compute_dtype=torch.float16,
                    bnb_4bit_use_double_quant=True,
                )
                kwargs = dict(quantization_config=bnb_config, device_map="auto")
            elif QUANT_MODE == "8bit":
                print("[sarvam] Loading model in 8-bit (bitsandbytes) ...")
                bnb_config = BitsAndBytesConfig(load_in_8bit=True)
                kwargs = dict(quantization_config=bnb_config, device_map="auto")
            elif QUANT_MODE == "cpu":
                print("[sarvam] Loading model on CPU (this will be slow) ...")
                kwargs = dict(torch_dtype=torch.float32, device_map="cpu")
            else:
                print("[sarvam] Loading model in full bf16 ...")
                kwargs = dict(torch_dtype=torch.bfloat16, device_map="auto")

            model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, **kwargs)

            import torch

            print("================================")
            print("CUDA:", torch.cuda.is_available())
            print("GPU:", torch.cuda.get_device_name(0))
            print("Model Device:", next(model.parameters()).device)
            print("================================")

            _tokenizer = tokenizer
            _model = model
            _load_status = "ready"
            print("[sarvam] Model ready.")
        except Exception as e:
            _load_error = str(e)
            _load_status = "error"
            print(f"[sarvam] FAILED to load model: {e}")


def ensure_model_loading_started():
    if _load_status == "not_started":
        threading.Thread(target=load_model, daemon=True).start()


# Kick off loading as soon as the server starts (in background) so the first
# real request doesn't have to wait for the whole download/load from scratch.
ensure_model_loading_started()


# ─────────────────────────────────────────────────────────────────────────────
# Generation (streaming)
# ─────────────────────────────────────────────────────────────────────────────
def stream_generate(prompt_text, enable_thinking=False):
    """
    Generator that yields SSE-formatted chunks of generated text as they're produced.
    """
    import torch
    from transformers import TextIteratorStreamer

    # messages = [{"role": "user", "content": prompt_text}]
    # messages = [
    #     {
    #         "role": "system",
    #         "content": "You are a professional translator. Return only translated text."
    #     },
    #     {
    #         "role": "user",
    #         "content": prompt_text
    #     }
    # ]

    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert translator. "
                "Translate the user's text into the requested language. "
                "Return only the translation. "
                "Do not explain. "
                "Do not output instructions. "
                "Do not output rules."
            )
        },
        {
            "role": "user",
            "content": prompt_text
        }
    ]


    chat_text = _tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=enable_thinking,
    )
    inputs = _tokenizer(chat_text, return_tensors="pt").to(_model.device)

    streamer = TextIteratorStreamer(_tokenizer, skip_prompt=True, skip_special_tokens=True)


    # generation_kwargs = dict(
    #     **inputs,
    #     max_new_tokens=64,
    #     do_sample=False,
    #     num_beams=1,
    #     repetition_penalty=1.0,
    #     eos_token_id=_tokenizer.eos_token_id,
    #     pad_token_id=_tokenizer.eos_token_id,
    #     streamer=streamer,
    # )

    generation_kwargs = dict(
        **inputs,
        max_new_tokens=256,
        do_sample=False,
        num_beams=1,
        repetition_penalty=1.05,
        eos_token_id=_tokenizer.eos_token_id,
        pad_token_id=_tokenizer.eos_token_id,
        streamer=streamer,
    )

    thread = threading.Thread(target=_model.generate, kwargs=generation_kwargs)
    thread.start()

    for new_text in streamer:
        if new_text:
            yield f"data: {json.dumps({'token': new_text})}\n\n"

    thread.join()
    yield f"data: {json.dumps({'done': True})}\n\n"


def sse_error(message):
    yield f"data: {json.dumps({'error': message})}\n\n"


# ─────────────────────────────────────────────────────────────────────────────
# Routes
# ─────────────────────────────────────────────────────────────────────────────
@app.route("/")
def index():
    return send_from_directory("public", "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("public", path)


@app.route("/api/status")
def status():
    return {
        "status": _load_status,
        "model": MODEL_NAME,
        "quant": QUANT_MODE,
        "error": _load_error,
    }


@app.route("/api/translate", methods=["POST"])
def translate():
    data = request.get_json(force=True)
    text = (data.get("text") or "").strip()
    language = data.get("language", "Hindi")
    mode = data.get("mode", "fresh")

    if not text:
        return {"error": "No text provided"}, 400

    if _load_status != "ready":
        ensure_model_loading_started()
        return {"error": f"Model not ready yet (status: {_load_status}). "
                          f"First load can take a few minutes while weights download/load. "
                          f"{_load_error or ''}"}, 503

    # prompt = build_translate_prompt(language, mode, text)
    # return Response(stream_generate(prompt), mimetype="text/event-stream",
    #                  headers={"Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*"})

    prompt = build_translate_prompt(language, mode, text)

    print("\n====================")
    print(prompt)
    print("====================\n")

    return Response(
        stream_generate(prompt),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Access-Control-Allow-Origin": "*"
        }
    )


@app.route("/api/review", methods=["POST"])
def review():
    data = request.get_json(force=True)
    english = (data.get("english") or "").strip()
    translated = (data.get("translated") or "").strip()
    language = data.get("language", "Hindi")

    if not english or not translated:
        return {"error": "Missing english or translated text"}, 400

    if _load_status != "ready":
        ensure_model_loading_started()
        return {"error": f"Model not ready yet (status: {_load_status}). "
                          f"{_load_error or ''}"}, 503

    prompt = build_review_prompt(language, english, translated)
    return Response(stream_generate(prompt), mimetype="text/event-stream",
                     headers={"Cache-Control": "no-cache", "Access-Control-Allow-Origin": "*"})


if __name__ == "__main__":
    print(f"\n{'='*70}")
    print(f"  AGM Translator (Hugging Face Transformers + {MODEL_NAME})")
    print(f"  Quantization: {QUANT_MODE}")
    print(f"  Model loading in background — first request may need to wait.")
    print(f"  Open: http://localhost:{PORT}")
    print(f"{'='*70}\n")
    app.run(host="0.0.0.0", port=PORT, threaded=True)
