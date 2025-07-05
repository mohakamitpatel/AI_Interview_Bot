import os
import json
import requests  # type: ignore
from dotenv import load_dotenv  # type: ignore

# Load API Key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def soften_score(raw_score):
    """Slightly curve the score to be more forgiving and scale it to 5."""
    curved = raw_score + (1.0 - raw_score) * 0.25  # Curve towards 1
    scaled_score = curved * 5                      # Scale to 5
    return round(min(scaled_score, 5.0), 2)

def generate_feedback_and_score(answer, question):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are an AI interview evaluator with a constructive and supportive tone.

A candidate responded to the following question:

Question: {question}
Answer: {answer}

Evaluate the answer and return only a JSON object with:
- "feedback": A brief encouraging and helpful comment (avoid harsh critique).
- "score": A float between 0.0 and 1.0 representing how well the answer addresses the question.

Only respond in this strict JSON format:
{{"feedback": "Clear explanation but could include more detail.", "score": 0.75}}
"""

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "You are an expert interview feedback generator."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        content = response.json()["choices"][0]["message"]["content"]

        # Try to parse JSON safely
        result = json.loads(content.strip())
        score = soften_score(float(result["score"]))
        return result["feedback"], score

    except Exception as e:
        print("⚠️ Groq API error or invalid response:", e)
        return "❌ Error generating feedback.", 0.0
