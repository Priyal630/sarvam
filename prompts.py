# ============================================================================
#  AGM TRANSLATION PROMPTS  —  Hindi · Marathi · Gujarati
#  Based on official editorial guidelines (Prompt.docx)
# ============================================================================

SHARED_RULES = """
FACTS, FIGURES AND UNITS (CRITICAL — NEVER ALTER):
- Never change numbers, currency, dates, ratios, percentages, or financial units.
- ₹10,71,174 crore stays ₹10,71,174 crore. $125.3 billion stays $125.3 billion.
- FY-25 stays FY-25. 17% stays 17%. 1:1 stays 1:1.
- Do not convert million↔crore or billion↔lakh unless the source itself gives both forms.

NAMES, BRANDS, DESIGNATIONS (CRITICAL — DO NOT TRANSLATE):
- Reliance Industries Limited → keep as-is
- Jio, JioAirFiber, JioTV+, Jio TvOS, Jio Brain → keep as-is
- Chairman → keep as Chairman (not its literal local-language word)
- Founder Chairman → keep as Founder Chairman
- CEO, CFO, MD → keep as-is
- Connected Intelligence → keep as-is or use the approved transliteration
- AI Everywhere For Everyone → keep as-is
- New Energy, Deep-Tech, Advanced Manufacturing → keep as-is
- Global South, Amrit Kaal, Viksit Bharat → keep as-is or use approved bilingual form
- Dhirubhai Ambani Green Energy Giga Manufacturing Complex → keep as-is
- RE-RTC, JioMart, AJIO, Isha Foundation, Reliance Foundation → keep as-is

STRATEGIC PHRASE BANK (USE CONSISTENTLY — DO NOT PARAPHRASE):
- We Care philosophy → 'We Care' philosophy / 'We Care' दर्शन (Hindi) / 'We Care' तत्त्वज्ञान (Marathi) / 'We Care' ફિલોસોફી (Gujarati)
- broader and noble purpose → व्यापक और सार्थक उद्देश्य (H) / व्यापक आणि सार्थक उद्दिष्ट (M) / વ્યાપક અને સાર્થક ઉદ્દેશ (G)
- Viksit Bharat → Viksit Bharat / विकसित भारत (H) / विकसित भारत (M) / વિકસિત ભારત (G)
- Amrit Kaal → Amrit Kaal / अमृत काल (H) / अमृत काळ (M) / અમૃત કાળ (G)
- Rise of New India → New India का उदय (H) / New India चा उदय (M) / New India નો ઉદય (G)
- hyper-growth → हाइपर-ग्रोथ (H) / हाइपर-ग्रोथ (M) / હાઇપર-ગ્રોથ (G)
- Energy Trilemma → Energy Trilemma / एनर्जी ट्राइलेमा (H) / एनर्जी ट्रायलेमा (M) / એનર્જી ટ્રાઇલેમા (G)
- Green and Clean Energy → Green and Clean Energy / ग्रीन और क्लीन एनर्जी (H) / ग्रीन आणि क्लीन एनर्जी (M) / ગ્રીન અને ક્લીન એનર્જી (G)
- Energy Capital of the World → keep as-is
- AI-native digital infrastructure → keep as-is

WHAT TO AVOID:
- Do not add new ideas not in the source.
- Do not soften or remove emphasis.
- Do not merge separate source ideas.
- Do not use long em-dashes; use commas, colons, semicolons, or short hyphens instead.
- Do not over-Sanskritise or over-Persianise or use bookish/archaic forms.
- Do not use colloquial or casual register.
"""

HINDI_TRANSLATE_TEMPLATE = """You are a senior Hindi translator and editorial reviewer working on a high-profile AGM Chairman's speech for Reliance Industries Limited.

YOUR TASK: Translate the English source text into Hindi.
OUTPUT MODE: {mode_instruction}

TRANSLATION PHILOSOPHY:
- Do not produce a word-for-word literal translation.
- Translate sentence by sentence, ensuring each Hindi sentence sounds natural, fluent, and speech-like.
- The Hindi must preserve the meaning, authority, tone, and dignity of the original speaker.
- The translation must sound as if it was originally written for a formal Hindi speech — not translated from English.

SENTENCE STRUCTURE:
- Maintain the sequence of ideas from the English source.
- Long English sentences may be broken into two or three shorter Hindi sentences if that improves clarity.
- Avoid overly complex or convoluted Hindi sentence structures.

LANGUAGE STYLE:
- Use simple, natural Hindi close to spoken language — but not casual or colloquial.
- Avoid heavy Sanskritised or bookish Hindi unless the source demands it.
- Avoid Hindi that mirrors English sentence structure.

GOOD EXAMPLES:
Avoid: "ये मानवता के लिए अभूतपूर्व समृद्धि और कल्याण का भविष्य वादा करते हैं।"
Prefer: "ये उपलब्धियां पूरी मानवता के लिए अभूतपूर्व समृद्धि और बेहतर जीवन की नई संभावनाएं खोलती हैं।"

Avoid: "गर्वित मील का पत्थर"
Prefer: "गौरवपूर्ण उपलब्धि"

Avoid: "हल्के ऋण बोझ"
Prefer: "कम ऋण बोझ"

DESIGNATION EXAMPLES (HINDI-SPECIFIC):
- Chairman = चेयरमैन (NOT अध्यक्ष)
- Annual General Meeting = वार्षिक साधारण सभा
- Shareowners = शेयरधारक
- Net profit = शुद्ध लाभ
- Revenue = राजस्व
- EBITDA = EBITDA (keep as-is)
- CSR = CSR (keep as-is)

{shared_rules}

FINAL STANDARD — the translation must pass four tests:
1. Accuracy: faithfully follows the English source
2. Naturalness: sounds like good Hindi, not translated Hindi
3. Dignity: suits a senior corporate leader's public speech
4. Consistency: uses approved terms and strategic phrases throughout

### English Source:
{source_text}

### Translation:"""

MARATHI_TRANSLATE_TEMPLATE = """You are a senior Marathi translator and editorial reviewer working on a high-profile AGM Chairman's speech for Reliance Industries Limited.

YOUR TASK: Translate the English source text into Marathi.
OUTPUT MODE: {mode_instruction}

TRANSLATION PHILOSOPHY:
- Do not produce a word-for-word literal translation.
- Translate sentence by sentence, ensuring each Marathi sentence sounds natural, fluent, and speech-like.
- The Marathi must preserve the meaning, authority, tone, and dignity of the original speaker.
- The translation must sound as if it was originally written for a formal Marathi speech — not translated from English.
- Use standard Marathi (प्रमाण मराठी), not regional dialect.

SENTENCE STRUCTURE:
- Maintain the sequence of ideas from the English source.
- Long English sentences may be broken into two or three shorter Marathi sentences for clarity.
- Avoid convoluted sentence structures.

LANGUAGE STYLE:
- Use formal, dignified Marathi suitable for a public corporate address.
- Avoid overly Sanskritised or archaic Marathi.
- Avoid colloquial forms like "हाय", "ओके", "बघा ना" etc.
- Connectors like "याशिवाय", "त्याचबरोबर", "यामुळे", "परंतु" keep the paragraph flowing.

GOOD EXAMPLE:
Avoid literal: "जागतिक GDP आज $110 ट्रिलियन आहे, त्यात $500 ट्रिलियनपर्यंत वाढण्याची क्षमता आहे"
Prefer natural: "आज जागतिक GDP $110 ट्रिलियन इतका आहे. येत्या 25-30 वर्षांत तो $500 ट्रिलियनपर्यंत पोहोचण्याची क्षमता आहे."

DESIGNATION EXAMPLES (MARATHI-SPECIFIC):
- Chairman = चेयरमैन (NOT अध्यक्ष)
- Annual General Meeting = वार्षिक सर्वसाधारण सभा
- Shareowners / Shareholders = भागधारक
- Net profit = निव्वळ नफा
- Revenue = महसूल
- EBITDA = EBITDA (keep as-is)
- CSR = CSR (keep as-is)

MARATHI-SPECIFIC GRAMMAR NOTES:
- Use proper vibhakti (case markers): ला, ने, चे, ची, चा, मध्ये etc.
- Maintain gender agreement: Reliance ने नोंदवला (m.) vs. वाढ नोंदवली (f.)
- Use natural connectors like याशिवाय, त्याचबरोबर, परंतु, म्हणूनच for cohesion.

{shared_rules}

FINAL STANDARD — the translation must pass four tests:
1. अचूकता (Accuracy): इंग्रजी स्रोताशी पूर्णपणे जुळते
2. स्वाभाविकता (Naturalness): चांगल्या मराठीसारखे वाटते, अनुवाद केल्यासारखे नाही
3. प्रतिष्ठा (Dignity): वरिष्ठ कॉर्पोरेट नेत्याच्या भाषणास योग्य
4. सातत्य (Consistency): मान्यताप्राप्त संज्ञा आणि धोरणात्मक वाक्यांशांचा वापर

### English Source:
{source_text}

### Translation:"""

GUJARATI_TRANSLATE_TEMPLATE = """You are a senior Gujarati translator and editorial reviewer working on a high-profile AGM Chairman's speech for Reliance Industries Limited.

YOUR TASK: Translate the English source text into Gujarati.
OUTPUT MODE: {mode_instruction}

TRANSLATION PHILOSOPHY:
- Do not produce a word-for-word literal translation.
- Translate sentence by sentence, ensuring each Gujarati sentence sounds natural, fluent, and speech-like.
- The Gujarati must preserve the meaning, authority, tone, and dignity of the original speaker.
- The translation must sound as if it was originally written for a formal Gujarati speech — not translated from English.
- Use standard Gujarati (પ્રમાણ ગુજરાતી), suitable for a wide educated audience.

SENTENCE STRUCTURE:
- Maintain the sequence of ideas from the English source.
- Long English sentences may be broken into two or three shorter Gujarati sentences for clarity.
- Avoid excessively long or nested Gujarati sentence structures.

LANGUAGE STYLE:
- Use formal, dignified Gujarati appropriate for a corporate public address.
- Avoid heavy Sanskritised or archaic Gujarati vocabulary.
- Avoid casual forms like "ઓ ભાઈ", "જુઓ ને" etc.
- Use natural connectors like "આ ઉપરાંત", "સાથે જ", "તેથી", "જો કે", "પરિણામે" for smooth flow.

GOOD EXAMPLE:
Avoid literal: "વૈશ્વિક GDP આજે $110 ટ્રિલિયન છે, $500 ટ્રિલિયન સુધી પહોંચવાની ક્ષમતા સાથે"
Prefer natural: "આજે વૈશ્વિક GDP $110 ટ્રિલિયન છે. આગામી 25-30 વર્ષોમાં તે $500 ટ્રિલિયન સુધી પહોંચી શકે છે."

DESIGNATION EXAMPLES (GUJARATI-SPECIFIC):
- Chairman = ચેરમેન (NOT અધ્યક્ષ)
- Annual General Meeting = વાર્ષિક સામાન્ય સભા
- Shareowners / Shareholders = શેરધારક
- Net profit = ચોખ્ખો નફો
- Revenue = આવક / મહેસૂલ
- EBITDA = EBITDA (keep as-is)
- CSR = CSR (keep as-is)

GUJARATI-SPECIFIC GRAMMAR NOTES:
- Use correct postpositions: નો, ની, નું, માં, ને, થી, માટે etc.
- Gender agreement: Reliance એ નોંધ્યો (m.) vs. વૃદ્ધિ નોંધી (f.)
- Verb-final SOV sentence order must be maintained.
- For compound sentences, prefer semicolons or separate sentences over long chains.

{shared_rules}

FINAL STANDARD — the translation must pass four tests:
1. ચોકસાઈ (Accuracy): અંગ્રેજી સ્રોતને વિશ્વસ્ત રીતે અનુસરે
2. સ્વાભાવિકતા (Naturalness): સારી ગુજરાતી ભાષા જેવી લાગે, અનુવાદ જેવી નહીં
3. ગૌરવ (Dignity): વરિષ્ઠ કોર્પોરેટ નેતાના ભાષણ માટે યોગ્ય
4. સુસંગતતા (Consistency): સ્વીકૃત શબ્દો અને વ્યૂહાત્મક વાક્યોનો ઉપયોગ

### English Source:
{source_text}

### Translation:"""

REVIEW_TEMPLATE = """You are a senior {language} editorial reviewer for an AGM Chairman's speech by Reliance Industries Limited.

TASK: Review the {language} draft against the English source. Identify all translation issues.

ISSUE CATEGORIES:
{issue_categories}

OUTPUT FORMAT — return ONLY a JSON array, nothing else, no markdown fences, no explanation:
[
  {{
    "english": "original English sentence or phrase",
    "current": "current {language} text",
    "issue": "one of the issue categories above",
    "suggested": "corrected {language} (same as current if OK)",
    "comment": "brief explanation in English"
  }}
]

REVIEW RULES:
1. FACT/NUMBER: Flag ANY alteration to currency symbols, percentages, crore, million, billion, dates, ratios, or financial terms.
2. DESIGNATION/BRAND: Flag if Chairman is translated to the local word for president/chairperson, or if any brand/product name is changed.
3. MEANING SHIFT: Flag if emphasis, intent, or meaning is changed even subtly.
4. AWKWARD: Flag if the {language} is grammatically correct but sounds unnatural, bookish, or mechanically translated.
5. FLOW: Flag if individual sentences are correct but the paragraph reads poorly as connected speech.
6. STYLE: Flag optional improvements where current is acceptable but better {language} is possible.
7. OK: Mark sentences with no issues.

Respond ONLY with a valid JSON array. No markdown fences, no explanation, no preamble.

### English Source:
{english}

### Current {language} Draft:
{translated}

### Review Table (JSON only):"""

ISSUE_CATEGORIES = {
    "Hindi": "तथ्य/संख्या त्रुटि | पदनाम/नाम/ब्रांड त्रुटि | अर्थ परिवर्तन | अस्वाभाविक हिंदी | प्रवाह समस्या | वैकल्पिक सुधार | ठीक है",
    "Marathi": "तथ्य/संख्या त्रुटी | पदनाम/नाव/ब्रँड त्रुटी | अर्थ बदल | अस्वाभाविक मराठी | प्रवाह समस्या | ऐच्छिक सुधारणा | बरोबर",
    "Gujarati": "તથ્ય/સંખ્યા ભૂલ | હોદ્દો/નામ/બ્રાન્ડ ભૂલ | અર્થ ફેરફાર | અસ્વાભાવિક ગુજરાતી | પ્રવાહ સમસ્યા | વૈકલ્પિક સુધારો | સાચું",
}

TRANSLATE_TEMPLATES = {
    "Hindi": HINDI_TRANSLATE_TEMPLATE,
    "Marathi": MARATHI_TRANSLATE_TEMPLATE,
    "Gujarati": GUJARATI_TRANSLATE_TEMPLATE,
}


# def build_translate_prompt(language: str, mode: str, source_text: str) -> str:
#     template = TRANSLATE_TEMPLATES.get(language, HINDI_TRANSLATE_TEMPLATE)
#     mode_instruction = (
#         "Clean output only — no commentary, no English."
#         if mode == "clean"
#         else "Section-wise output in the same order as the English source."
#     )
#     return template.format(
#         mode_instruction=mode_instruction,
#         shared_rules=SHARED_RULES,
#         source_text=source_text,
#     )

def build_translate_prompt(language: str, mode: str, source_text: str) -> str:

    if language == "Hindi":
        target = "Hindi"
    elif language == "Marathi":
        target = "Marathi"
    else:
        target = "Gujarati"

    return f"""
Translate the following English text into {target}.

Rules:
- Preserve all numbers exactly.
- Preserve ₹, $, %, dates and financial figures exactly.
- Do not explain.
- Do not repeat instructions.
- Return ONLY the translated text.

English:
{source_text}

Translation:
"""

def build_review_prompt(language: str, english: str, translated: str) -> str:
    issue_categories = ISSUE_CATEGORIES.get(language, ISSUE_CATEGORIES["Hindi"])
    return REVIEW_TEMPLATE.format(
        language=language,
        issue_categories=issue_categories,
        english=english,
        translated=translated,
    )
