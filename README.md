<div align="center">

<img src="https://code.swecha.org/Sohansourab27/campusgpt/-/raw/main/WhatsApp_Image_2026-06-10_at_21.39.02.jpeg" width="500" alt="CampusGPT Logo" />

<br/>

<p><em>Your all-in-one AI companion for academic and career success.</em></p>

[![Live App](https://img.shields.io/badge/🚀%20Live%20App-campus--gpt.streamlit.app-B8D651?style=for-the-badge&logo=streamlit&logoColor=white)](https://campus-gpt.streamlit.app/)

`Streamlit` &nbsp;•&nbsp; `Groq LPU` &nbsp;•&nbsp; `LLaMA 3.1` &nbsp;•&nbsp; `pypdf` &nbsp;•&nbsp; `Python 3.9+`

</div>

---

## What is CampusGPT?

CampusGPT is an AI-powered student success platform built with **Streamlit** and **LLaMA 3.1** via the **Groq** inference API. It gives students four independent career and academic tools in a single tabbed interface — no sign-in, no setup friction.

| Module | What it does |
|---|---|
| 📄 **PDF Assistant** | Upload any PDF and ask questions grounded strictly in its content |
| 📑 **Resume Analyzer** | Get an ATS score, key skills, strengths, gaps, and improvement tips |
| 🎤 **Interview Simulator** | Generate role-specific questions and receive AI feedback on your answers |
| 🛣️ **Career Roadmap** | Get a personalized month-by-month learning and career plan |

---

## ✨ New Features

| Feature | Description |
|---|---|
| 🔑 **BYOK** | Bring Your Own Key — paste your Groq API key directly in the sidebar, no `.env` needed |
| 🦙 **Ollama Local Inference** | Switch to fully offline, on-device AI using Ollama — no internet, no API key, full privacy |
| 🌐 **i18n / l10n** | Full internationalisation in 3 languages — 🇬🇧 English, 🇮🇳 हिन्दी, 🇮🇳 తెలుగు |

---

## Architecture

![CampusGPT System Architecture](https://github.com/sohansourab/campusGPT-replit/blob/main/arch.png?raw=true)

> **Backend flow (common to all modules):**
> `Streamlit UI` → `app.py` → `utils/` (pdf_utils + groq_helper) → `Groq API (LLaMA 3.1)` **or** `Ollama (Local)` → `AI Response` → `UI Output`

---

## Tech Stack

| Layer | Tool |
|---|---|
| UI | Streamlit ≥ 1.35 |
| LLM Inference (Cloud) | Groq API — `llama-3.1-8b-instant` |
| LLM Inference (Local) | Ollama — `llama3.2` (or any pulled model) |
| PDF Parsing | pypdf ≥ 4.0 |
| HTTP (Ollama) | requests ≥ 2.31 |
| Config | python-dotenv |
| Runtime | Python 3.9+ |

---

## Local Setup

```bash
# 1. Clone
git clone https://github.com/sohansourab/campusGPT-replit.git
cd campusGPT-replit

# 2. Install dependencies
pip install -r requirements.txt

# 3. Environment
cp .env.example .env
# Edit .env and add your key:
# GROQ_API_KEY=your_key_here

# 4. Run
streamlit run app.py
```

> Get a free Groq API key at [console.groq.com](https://console.groq.com)

---

## Running with Ollama (Fully Offline)

```bash
# 1. Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. Pull a model
ollama pull llama3.2

# 3. Start Ollama server (keep this terminal open)
ollama serve

# 4. In a new terminal, run the app
streamlit run app.py
```

Then in the sidebar:
- Select **Ollama (Local)**
- URL: `http://localhost:11434`
- Model: `llama3.2`
- Click **Check Ollama Status** → ✅

> No API key required. Works completely offline.

---

## Streamlit Cloud Deployment

1. Push repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select repo · branch `main` · file `app.py`
4. Add secret under **Settings → Secrets**:
```toml
GROQ_API_KEY = "your_key_here"
```

---

## Project Structure

```
campusgpt_streamlit/
├── app.py                     ← Entry point — tab layout, sidebar, i18n routing
├── modules/
│   ├── pdf_assistant.py       ← PDF Q&A module
│   ├── resume_analyzer.py     ← ATS scoring & feedback
│   ├── interview_simulator.py ← Question generation & answer evaluation
│   └── career_roadmap.py      ← Personalized career plan generator
├── utils/
│   ├── groq_helper.py         ← Groq + Ollama backend router (BYOK support)
│   └── pdf_utils.py           ← PDF text extraction via pypdf
├── i18n/
│   ├── __init__.py
│   └── translations.py        ← 150 strings × 3 locales (EN / HI / TE)
├── requirements.txt
├── .env.example
└── README.md
```

---

## i18n / l10n

CampusGPT supports **3 languages** switchable from the sidebar at runtime:

| Code | Language | Script |
|---|---|---|
| `en` | English | Latin |
| `hi` | Hindi | देवनागरी |
| `te` | Telugu | తెలుగు |

All UI strings — tab labels, buttons, placeholders, warnings, spinners — are routed through `t("key")` and translate instantly on language switch. LLM prompts remain in English for best model performance.

---

## Notes

- PDF content is capped at **~12,000 characters** to stay within LLM context limits.
- A **3-second cooldown** between API calls prevents rate-limit issues.
- No user data is stored — all processing is stateless and session-local.
- BYOK key is stored only in Streamlit session state — never persisted or transmitted elsewhere.

---

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

---

## License

[MIT](LICENSE)

---

<div align="center">

[![Live App](https://img.shields.io/badge/🚀%20Live%20App-campus--gpt.streamlit.app-B8D651?style=for-the-badge&logo=streamlit&logoColor=white)](https://campus-gpt.streamlit.app/)

</div>
