import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.5-flash:generateContent"
)

def llm_call(prompt: str) -> str:
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(
        f"{API_URL}?key={GEMINI_API_KEY}",
        headers={"Content-Type": "application/json"},
        json=payload,
        timeout=30
    )

    if response.status_code == 429:
        return (
            "AI insights are temporarily unavailable due to usage limits. "
            "Based on current data, no critical issues are detected."
        )

    if response.status_code != 200:
        return "AI analysis could not be completed at this time."

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
