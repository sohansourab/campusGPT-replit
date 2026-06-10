import os
import time
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# simple anti-spam lock (prevents Streamlit multiple calls)
last_call_time = 0

def ask_gemini(prompt):
    global last_call_time

    # prevent rapid repeated calls
    if time.time() - last_call_time < 3:
        return "⚠️ Please wait a few seconds before making another request."

    last_call_time = time.time()

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    except Exception:
        return "⚠️ Error occurred. Please try again."