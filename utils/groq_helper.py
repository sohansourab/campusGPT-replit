"""
utils/groq_helper.py
LLM backend wrapper for CampusGPT.
Supports:
  - Groq cloud API (default, with BYOK)
  - Ollama local inference (offline / privacy mode)
"""

import os
import time
import requests
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Simple anti-spam lock (prevents multiple rapid calls)
_last_call_time: float = 0

# ── Backend helpers ──────────────────────────────────────────────────

def _get_groq_key() -> str:
    """User BYOK key > env variable."""
    user_key = st.session_state.get("groq_api_key", "").strip()
    return user_key if user_key else os.getenv("GROQ_API_KEY", "")


def _ask_groq(prompt: str) -> str:
    api_key = _get_groq_key()
    if not api_key:
        return (
            "⚠️ No Groq API key found. Enter your key in the sidebar, "
            "or switch to Ollama for local inference."
        )
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def _ask_ollama(prompt: str) -> str:
    base_url = st.session_state.get("ollama_url", "http://localhost:11434").rstrip("/")
    model    = st.session_state.get("ollama_model", "llama3.2").strip() or "llama3.2"

    try:
        resp = requests.post(
            f"{base_url}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=120,
        )
        resp.raise_for_status()
        return resp.json().get("response", "⚠️ Empty response from Ollama.")
    except requests.exceptions.ConnectionError:
        return (
            f"⚠️ Cannot connect to Ollama at `{base_url}`. "
            "Make sure Ollama is running (`ollama serve`) and the URL is correct."
        )
    except requests.exceptions.Timeout:
        return "⚠️ Ollama request timed out. The model may still be loading — try again."
    except Exception as e:
        return f"⚠️ Ollama error: {e}"


# ── Public API ───────────────────────────────────────────────────────

def check_ollama_status(base_url: str) -> tuple[bool, str]:
    """Ping Ollama and return (is_running, status_message)."""
    try:
        resp = requests.get(f"{base_url.rstrip('/')}/api/tags", timeout=4)
        resp.raise_for_status()
        models = [m["name"] for m in resp.json().get("models", [])]
        if models:
            return True, f"Running · {len(models)} model(s): {', '.join(models[:4])}"
        return True, "Running · no models pulled yet (`ollama pull llama3.2`)"
    except Exception:
        return False, "Not reachable"


def ask_llm(prompt: str) -> str:
    """
    Route the prompt to the active backend (Groq or Ollama).
    Applies a 3-second cooldown between requests.
    """
    global _last_call_time

    if time.time() - _last_call_time < 3:
        return "⚠️ Please wait a few seconds before making another request."
    _last_call_time = time.time()

    backend = st.session_state.get("llm_backend", "Groq")
    try:
        if backend == "Ollama (Local)":
            return _ask_ollama(prompt)
        else:
            return _ask_groq(prompt)
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"
