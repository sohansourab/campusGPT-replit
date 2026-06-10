"""
utils/groq_helper.py
Wrapper around the Groq LLaMA API.
"""

import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Simple anti-spam lock (prevents multiple rapid calls)
_last_call_time: float = 0


def ask_llm(prompt: str) -> str:
    """
    Send a prompt to LLaMA via Groq and return the response text.
    Applies a 3-second cooldown between requests.
    """
    global _last_call_time

    if time.time() - _last_call_time < 3:
        return "⚠️ Please wait a few seconds before making another request."

    _last_call_time = time.time()

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error: {e}"
