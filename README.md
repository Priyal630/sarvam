# AGM Translation Tool — sarvam-m via Hugging Face Transformers (fully local)

No API keys, no internet calls at inference time. Runs `sarvamai/sarvam-m`
directly on your machine using Hugging Face `transformers`.

---

## ⚠️ Hardware reality check first

`sarvam-m` is a **~24B parameter** model (built on Mistral-Small). This is NOT
a small model — it needs real GPU memory:

| Mode          | VRAM needed       | Notes                                      |
|---------------|--------------------|---------------------------------------------|
| `4bit` (default) | **~14-16 GB**   | Works on RTX 3090 / 4090 / 4080 16GB        |
| `8bit`         | **~26-28 GB**     | Needs RTX 4090/A6000 or better              |
| `none` (bf16)  | **~48 GB**        | Datacenter GPUs only (A100/H100)            |
| `cpu`          | ~48 GB **system RAM** | Works without a GPU but very slow (minutes per response) |

**If you have an 8GB or 12GB consumer GPU** (e.g. RTX 3060/3070/4060), full
`sarvam-m` in 4-bit still won't comfortably fit. In that case, use the
smaller **`sarvamai/sarvam-2b`** model instead — see "Using a smaller model"
below. It's much faster and fits easily on 8GB cards, though translation
quality is lower than sarvam-m.

If you're unsure what GPU you have, run `nvidia-smi` in a terminal — it
shows your VRAM in the top-right of the table.

---

## Setup

### 1. Install Python dependencies

```bash
cd agm-translator-hf
pip install -r requirements.txt
```

If you're on Windows and `bitsandbytes` fails to install, see
"Troubleshooting" below — Windows support for bitsandbytes 4-bit/8-bit is
version-sensitive.

### 2. Log in to Hugging Face (first time only)

`sarvam-m` is a gated-free public model but you still need a HF account to
download it:

```bash
pip install huggingface_hub
huggingface-cli login
```

Paste your token from https://huggingface.co/settings/tokens (read access is enough).

### 3. Run the server

```bash
python server.py
```

The model starts loading in the background immediately. First run will
**download ~48GB of weights** (cached afterwards in `~/.cache/huggingface`),
then load them onto your GPU in 4-bit. This can take several minutes —
watch the terminal for progress.

Open: **http://localhost:5000**

The page polls `/api/status` every 3 seconds and shows a banner while the
model is loading. Once it says "ready", you're good to go.

---

## Using a smaller model (8GB/12GB GPUs, or CPU-only laptops)

Edit the model name via environment variable instead of changing code:

```bash
# Windows (cmd)
set SARVAM_MODEL=sarvamai/sarvam-2b
set SARVAM_QUANT=none
python server.py

# Windows (PowerShell)
$env:SARVAM_MODEL="sarvamai/sarvam-2b"
$env:SARVAM_QUANT="none"
python server.py

# macOS / Linux
SARVAM_MODEL=sarvamai/sarvam-2b SARVAM_QUANT=none python server.py
```

Note: `sarvam-2b` is NOT a great instruction-follower (it's primarily a base
/ completion model per its model card) — translations will be rougher than
`sarvam-m`. If quality matters more than speed, stick with `sarvam-m` in
4-bit and be patient with load time.

---

## Environment variables (all optional)

| Variable           | Default            | What it does                                    |
|---------------------|--------------------|-------------------------------------------------|
| `SARVAM_MODEL`       | `sarvamai/sarvam-m` | Which HF model to load                          |
| `SARVAM_QUANT`       | `4bit`              | `4bit` \| `8bit` \| `none` \| `cpu`              |
| `SARVAM_MAX_TOKENS`  | `1024`              | Max tokens generated per response               |
| `PORT`               | `5000`              | Server port                                     |

---

## Troubleshooting

**`bitsandbytes` install fails on Windows**
Use the Windows-specific wheel:
```bash
pip install bitsandbytes --index-url https://jllllll.github.io/bitsandbytes-windows-webui
```

**`CUDA out of memory`**
- Switch to `SARVAM_QUANT=4bit` if you weren't already
- Close other GPU programs (games, other model servers)
- Reduce `SARVAM_MAX_TOKENS` (e.g. to 512)
- If still failing, your GPU is too small for sarvam-m — use `sarvam-2b` instead

**Model loads but output looks like garbage / repeats itself**
- This is common with smaller/base models like `sarvam-2b` which aren't
  instruction-tuned the same way. Try lowering `temperature` in `server.py`
  (`stream_generate` function) or switch back to `sarvam-m`.

**"Model not ready yet" error keeps showing**
- Check the terminal running `server.py` — it prints load progress and any
  errors there. First-time downloads of ~48GB can take a long time depending
  on your internet connection.

**No NVIDIA GPU at all**
- Set `SARVAM_QUANT=cpu`. It will work but expect multi-minute response times.

---

## Files

```
agm-translator-hf/
├── server.py          # Flask server + Transformers model loading/inference
├── prompts.py          # All translation prompts (Hindi, Marathi, Gujarati)
├── requirements.txt
├── public/
│   └── index.html       # Full UI (same as before, talks to Flask instead of Node)
└── README.md
```

## What's inside the prompts

Same editorial rulebook as before, ported to Python string templates:
- Translation philosophy (natural, dignified, not literal)
- Facts & figures lockdown (₹, $, %, crore, billion, dates — never altered)
- Brand/designation lockdown (Chairman, Jio, Reliance Industries Limited, etc.)
- Strategic phrase bank (Viksit Bharat, Amrit Kaal, AI Everywhere For Everyone…)
- Language-specific grammar notes for Hindi, Marathi, Gujarati
- 6-category review system for draft checking
