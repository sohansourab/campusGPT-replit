"""
i18n/translations.py

Internationalisation (i18n) + Localisation (l10n) for CampusGPT.

i18n  = structuring the app so text is swappable (keys, not hardcoded strings)
l10n  = the actual translated content for each locale

Supported locales:
  en  — English
  hi  — Hindi (हिन्दी)
  te  — Telugu (తెలుగు)
"""

TRANSLATIONS: dict[str, dict[str, str]] = {

    # ── App-wide ─────────────────────────────────────────────────────
    "app_title": {
        "en": "CampusGPT",
        "hi": "CampusGPT",
        "te": "CampusGPT",
    },
    "app_subtitle": {
        "en": "AI-Powered Student Success Platform",
        "hi": "AI-संचालित छात्र सफलता मंच",
        "te": "AI-ఆధారిత విద్యార్థి విజయ వేదిక",
    },
    "sidebar_backend_title": {
        "en": "⚙️ AI Backend",
        "hi": "⚙️ AI बैकएंड",
        "te": "⚙️ AI బ్యాకెండ్",
    },
    "sidebar_backend_label": {
        "en": "Choose inference backend",
        "hi": "इन्फ़ेरेंस बैकएंड चुनें",
        "te": "ఇన్ఫరెన్స్ బ్యాకెండ్ ఎంచుకోండి",
    },
    "sidebar_language_label": {
        "en": "🌐 Language / भाषा / భాష",
        "hi": "🌐 भाषा",
        "te": "🌐 భాష",
    },
    "sidebar_groq_title": {
        "en": "### 🔑 Groq API Key (BYOK)",
        "hi": "### 🔑 Groq API कुंजी (BYOK)",
        "te": "### 🔑 Groq API కీ (BYOK)",
    },
    "sidebar_groq_server_key": {
        "en": "✅ Server key loaded",
        "hi": "✅ सर्वर कुंजी लोड हुई",
        "te": "✅ సర్వర్ కీ లోడ్ అయింది",
    },
    "sidebar_groq_override": {
        "en": "You can override it with your own key below.",
        "hi": "आप नीचे अपनी कुंजी से इसे बदल सकते हैं।",
        "te": "మీరు దిగువ మీ స్వంత కీతో దీన్ని భర్తీ చేయవచ్చు.",
    },
    "sidebar_groq_key_label": {
        "en": "Your Groq API Key",
        "hi": "आपकी Groq API कुंजी",
        "te": "మీ Groq API కీ",
    },
    "sidebar_groq_using_key": {
        "en": "✅ Using your key",
        "hi": "✅ आपकी कुंजी उपयोग हो रही है",
        "te": "✅ మీ కీ ఉపయోగిస్తున్నాం",
    },
    "sidebar_groq_no_key": {
        "en": "⚠️ No key set — enter one above",
        "hi": "⚠️ कोई कुंजी नहीं — ऊपर दर्ज करें",
        "te": "⚠️ కీ లేదు — పై నమోదు చేయండి",
    },
    "sidebar_groq_link": {
        "en": "[Get a free Groq key →](https://console.groq.com)",
        "hi": "[मुफ़्त Groq कुंजी पाएं →](https://console.groq.com)",
        "te": "[ఉచిత Groq కీ పొందండి →](https://console.groq.com)",
    },
    "sidebar_ollama_title": {
        "en": "### 🦙 Ollama Local Inference",
        "hi": "### 🦙 Ollama स्थानीय इन्फ़ेरेंस",
        "te": "### 🦙 Ollama స్థానిక ఇన్ఫరెన్స్",
    },
    "sidebar_ollama_url_label": {
        "en": "Ollama server URL",
        "hi": "Ollama सर्वर URL",
        "te": "Ollama సర్వర్ URL",
    },
    "sidebar_ollama_model_label": {
        "en": "Model name",
        "hi": "मॉडल का नाम",
        "te": "మోడల్ పేరు",
    },
    "sidebar_ollama_check_btn": {
        "en": "🔍 Check Ollama Status",
        "hi": "🔍 Ollama स्थिति जांचें",
        "te": "🔍 Ollama స్థితి తనిఖీ చేయండి",
    },
    "sidebar_ollama_pinging": {
        "en": "Pinging Ollama…",
        "hi": "Ollama को पिंग कर रहे हैं…",
        "te": "Ollama ని పింగ్ చేస్తున్నాం…",
    },

    # ── Home tab ─────────────────────────────────────────────────────
    "tab_home": {
        "en": "🏠 Home",
        "hi": "🏠 होम",
        "te": "🏠 హోమ్",
    },
    "tab_pdf": {
        "en": "📄 PDF Assistant",
        "hi": "📄 PDF सहायक",
        "te": "📄 PDF అసిస్టెంట్",
    },
    "tab_resume": {
        "en": "📑 Resume Analyzer",
        "hi": "📑 रेज़्यूमे विश्लेषक",
        "te": "📑 రెజ్యూమే విశ్లేషకుడు",
    },
    "tab_interview": {
        "en": "🎤 Interview Simulator",
        "hi": "🎤 इंटरव्यू सिम्युलेटर",
        "te": "🎤 ఇంటర్వ్యూ సిమ్యులేటర్",
    },
    "tab_roadmap": {
        "en": "🛣️ Career Roadmap",
        "hi": "🛣️ करियर रोडमैप",
        "te": "🛣️ కెరీర్ రోడ్‌మ్యాప్",
    },
    "home_welcome": {
        "en": "## Welcome to CampusGPT 👋\n\nYour all-in-one AI companion for academic and career success.\n\n| Module | Description |\n|---|---|\n| 📄 **PDF Assistant** | Upload any PDF and ask questions about its content |\n| 📑 **Resume Analyzer** | Get your ATS score, strengths, gaps & improvement tips |\n| 🎤 **Interview Simulator** | Practice role-specific interviews with AI feedback |\n| 🛣️ **Career Roadmap** | Receive a personalised, month-by-month learning plan |\n\n> **Tip:** Switch between **Groq (cloud)** and **Ollama (local)** in the sidebar anytime.",
        "hi": "## CampusGPT में आपका स्वागत है 👋\n\nशैक्षणिक और करियर सफलता के लिए आपका AI साथी।\n\n| मॉड्यूल | विवरण |\n|---|---|\n| 📄 **PDF सहायक** | कोई भी PDF अपलोड करें और उसके बारे में प्रश्न पूछें |\n| 📑 **रेज़्यूमे विश्लेषक** | ATS स्कोर, ताकत, कमियाँ और सुधार सुझाव पाएं |\n| 🎤 **इंटरव्यू सिम्युलेटर** | AI फ़ीडबैक के साथ भूमिका-विशिष्ट इंटरव्यू का अभ्यास करें |\n| 🛣️ **करियर रोडमैप** | व्यक्तिगत, महीने-दर-महीने सीखने की योजना पाएं |\n\n> **सुझाव:** साइडबार में कभी भी **Groq (क्लाउड)** और **Ollama (लोकल)** के बीच स्विच करें।",
        "te": "## CampusGPT కి స్వాగతం 👋\n\nవిద్యా మరియు కెరీర్ విజయానికి మీ AI తోడు.\n\n| మాడ్యూల్ | వివరణ |\n|---|---|\n| 📄 **PDF అసిస్టెంట్** | ఏదైనా PDF అప్‌లోడ్ చేసి దాని గురించి ప్రశ్నలు అడగండి |\n| 📑 **రెజ్యూమే విశ్లేషకుడు** | ATS స్కోర్, బలాలు, లోపాలు & మెరుగుదల చిట్కాలు పొందండి |\n| 🎤 **ఇంటర్వ్యూ సిమ్యులేటర్** | AI అభిప్రాయంతో పాత్ర-నిర్దిష్ట ఇంటర్వ్యూలు సాధన చేయండి |\n| 🛣️ **కెరీర్ రోడ్‌మ్యాప్** | నెల-వారీ వ్యక్తిగత అభ్యాస ప్రణాళిక పొందండి |\n\n> **చిట్కా:** సైడ్‌బార్‌లో ఎప్పుడైనా **Groq (క్లౌడ్)** మరియు **Ollama (స్థానిక)** మధ్య మారండి.",
    },

    # ── PDF Assistant ─────────────────────────────────────────────────
    "pdf_title": {
        "en": "## 📄 PDF Assistant\nUpload any PDF and ask questions about its content.",
        "hi": "## 📄 PDF सहायक\nकोई भी PDF अपलोड करें और उसके बारे में प्रश्न पूछें।",
        "te": "## 📄 PDF అసిస్టెంట్\nఏదైనా PDF అప్‌లోడ్ చేసి దాని గురించి ప్రశ్నలు అడగండి.",
    },
    "pdf_upload_label": {
        "en": "Upload PDF",
        "hi": "PDF अपलोड करें",
        "te": "PDF అప్‌లోడ్ చేయండి",
    },
    "pdf_question_label": {
        "en": "Your Question",
        "hi": "आपका प्रश्न",
        "te": "మీ ప్రశ్న",
    },
    "pdf_question_placeholder": {
        "en": "What is the main topic of this document?",
        "hi": "इस दस्तावेज़ का मुख्य विषय क्या है?",
        "te": "ఈ పత్రం యొక్క ప్రధాన అంశం ఏమిటి?",
    },
    "pdf_ask_btn": {
        "en": "Ask",
        "hi": "पूछें",
        "te": "అడగండి",
    },
    "pdf_warn_no_file": {
        "en": "⚠️ Please upload a PDF first.",
        "hi": "⚠️ कृपया पहले एक PDF अपलोड करें।",
        "te": "⚠️ దయచేసి మొదట PDF అప్‌లోడ్ చేయండి.",
    },
    "pdf_warn_no_question": {
        "en": "⚠️ Please enter a question.",
        "hi": "⚠️ कृपया एक प्रश्न दर्ज करें।",
        "te": "⚠️ దయచేసి ఒక ప్రశ్న నమోదు చేయండి.",
    },
    "pdf_warn_no_text": {
        "en": "⚠️ Could not extract text from this PDF.",
        "hi": "⚠️ इस PDF से टेक्स्ट निकाल नहीं सका।",
        "te": "⚠️ ఈ PDF నుండి టెక్స్ట్ తీయలేకపోయాం.",
    },
    "pdf_spinner": {
        "en": "Thinking…",
        "hi": "सोच रहे हैं…",
        "te": "ఆలోచిస్తున్నాం…",
    },

    # ── Resume Analyzer ───────────────────────────────────────────────
    "resume_title": {
        "en": "## 📑 Resume Analyzer\nGet an ATS score, strengths, weaknesses, and tailored improvement tips.",
        "hi": "## 📑 रेज़्यूमे विश्लेषक\nATS स्कोर, ताकत, कमियाँ और सुधार सुझाव पाएं।",
        "te": "## 📑 రెజ్యూమే విశ్లేషకుడు\nATS స్కోర్, బలాలు, బలహీనతలు మరియు మెరుగుదల చిట్కాలు పొందండి.",
    },
    "resume_upload_label": {
        "en": "Upload Resume (PDF)",
        "hi": "रेज़्यूमे अपलोड करें (PDF)",
        "te": "రెజ్యూమే అప్‌లోడ్ చేయండి (PDF)",
    },
    "resume_analyze_btn": {
        "en": "Analyze Resume",
        "hi": "रेज़्यूमे विश्लेषण करें",
        "te": "రెజ్యూమే విశ్లేషించండి",
    },
    "resume_warn_no_file": {
        "en": "⚠️ Please upload your resume as a PDF.",
        "hi": "⚠️ कृपया अपना रेज़्यूमे PDF के रूप में अपलोड करें।",
        "te": "⚠️ దయచేసి మీ రెజ్యూమేను PDF గా అప్‌లోడ్ చేయండి.",
    },
    "resume_warn_no_text": {
        "en": "⚠️ Could not extract text from this PDF.",
        "hi": "⚠️ इस PDF से टेक्स्ट निकाल नहीं सका।",
        "te": "⚠️ ఈ PDF నుండి టెక్స్ట్ తీయలేకపోయాం.",
    },
    "resume_spinner": {
        "en": "Analyzing…",
        "hi": "विश्लेषण हो रहा है…",
        "te": "విశ్లేషిస్తున్నాం…",
    },

    # ── Interview Simulator ───────────────────────────────────────────
    "interview_title": {
        "en": "## 🎤 Interview Simulator\nPractice role-specific interviews and get AI feedback on your answers.",
        "hi": "## 🎤 इंटरव्यू सिम्युलेटर\nभूमिका-विशिष्ट इंटरव्यू का अभ्यास करें और AI फ़ीडबैक पाएं।",
        "te": "## 🎤 ఇంటర్వ్యూ సిమ్యులేటర్\nపాత్ర-నిర్దిష్ట ఇంటర్వ్యూలు సాధన చేసి AI అభిప్రాయం పొందండి.",
    },
    "interview_role_label": {
        "en": "Select Role",
        "hi": "भूमिका चुनें",
        "te": "పాత్ర ఎంచుకోండి",
    },
    "interview_gen_btn": {
        "en": "Generate Questions",
        "hi": "प्रश्न उत्पन्न करें",
        "te": "ప్రశ్నలు రూపొందించండి",
    },
    "interview_gen_spinner": {
        "en": "Generating questions…",
        "hi": "प्रश्न बना रहे हैं…",
        "te": "ప్రశ్నలు రూపొందిస్తున్నాం…",
    },
    "interview_eval_heading": {
        "en": "### ✍️ Answer Evaluation",
        "hi": "### ✍️ उत्तर मूल्यांकन",
        "te": "### ✍️ సమాధాన మూల్యాంకనం",
    },
    "interview_answer_label": {
        "en": "Your Answer",
        "hi": "आपका उत्तर",
        "te": "మీ సమాధానం",
    },
    "interview_answer_placeholder": {
        "en": "Type your answer to one of the questions above…",
        "hi": "ऊपर दिए किसी प्रश्न का उत्तर टाइप करें…",
        "te": "పై ప్రశ్నలలో దేనికైనా మీ సమాధానం టైప్ చేయండి…",
    },
    "interview_eval_btn": {
        "en": "Evaluate Answer",
        "hi": "उत्तर मूल्यांकन करें",
        "te": "సమాధానం మూల్యాంకనం చేయండి",
    },
    "interview_eval_spinner": {
        "en": "Evaluating…",
        "hi": "मूल्यांकन हो रहा है…",
        "te": "మూల్యాంకనం చేస్తున్నాం…",
    },

    # ── Career Roadmap ────────────────────────────────────────────────
    "roadmap_title": {
        "en": "## 🛣️ Career Roadmap Generator\nGet a personalized, step-by-step plan to reach your career goal.",
        "hi": "## 🛣️ करियर रोडमैप जनरेटर\nअपने करियर लक्ष्य तक पहुँचने के लिए व्यक्तिगत, चरण-दर-चरण योजना पाएं।",
        "te": "## 🛣️ కెరీర్ రోడ్‌మ్యాప్ జెనరేటర్\nమీ కెరీర్ లక్ష్యాన్ని చేరుకోవడానికి వ్యక్తిగత, దశల వారీ ప్రణాళిక పొందండి.",
    },
    "roadmap_goal_label": {
        "en": "Career Goal",
        "hi": "करियर लक्ष्य",
        "te": "కెరీర్ లక్ష్యం",
    },
    "roadmap_goal_placeholder": {
        "en": "e.g. Machine Learning Engineer, Full Stack Developer, Data Scientist…",
        "hi": "जैसे Machine Learning Engineer, Full Stack Developer, Data Scientist…",
        "te": "ఉదా. Machine Learning Engineer, Full Stack Developer, Data Scientist…",
    },
    "roadmap_gen_btn": {
        "en": "Generate Roadmap",
        "hi": "रोडमैप बनाएं",
        "te": "రోడ్‌మ్యాప్ రూపొందించండి",
    },
    "roadmap_warn_no_goal": {
        "en": "⚠️ Please enter a career goal.",
        "hi": "⚠️ कृपया एक करियर लक्ष्य दर्ज करें।",
        "te": "⚠️ దయచేసి కెరీర్ లక్ష్యాన్ని నమోదు చేయండి.",
    },
    "roadmap_spinner": {
        "en": "Building your roadmap…",
        "hi": "आपका रोडमैप बना रहे हैं…",
        "te": "మీ రోడ్‌మ్యాప్ నిర్మిస్తున్నాం…",
    },
}


def t(key: str) -> str:
    """
    Translate a key to the active locale stored in Streamlit session state.
    Falls back to English if the key or locale is missing.
    """
    import streamlit as st
    locale = st.session_state.get("locale", "en")
    entry = TRANSLATIONS.get(key, {})
    return entry.get(locale) or entry.get("en") or key
