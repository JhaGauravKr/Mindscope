import json
import re
from typing import List
from groq import Groq

# ───── Get Groq Client ─────
def _get_client(api_key: str) -> Groq:
    return Groq(api_key=api_key)

# ───── Generate Subjective Questions ─────
def generate_subjective_questions(document_text: str, api_key: str, num_questions: int = 3) -> List[str]:
    client = _get_client(api_key)

    prompt = (
        f"You are a helpful academic assistant. From the following document, generate {num_questions} purely subjective, open-ended questions. "
        f"These questions should not contain multiple-choice options, correct answers, or justifications. "
        f"Only return the questions as a numbered list in plain text format.\n\n"
        f"DOCUMENT:\n{document_text[:8000]}"
    )

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500,
            top_p=1
        )

        raw = response.choices[0].message.content.strip()

        questions = [
            re.sub(r"^\s*\d+[\).]?\s*", "", line).strip()
            for line in raw.splitlines()
            if line.strip() and re.match(r"^\d+[\).]?\s+", line)
        ]

        return questions[:num_questions]

    except Exception as e:
        raise RuntimeError(f"❌ Subjective question generation error: {e}")

def evaluate_subjective(user_answer: str, question: str, api_key: str) -> str:
    client = _get_client(api_key)

    prompt = (
        "You are an evaluator. Read the question and the student's answer carefully. "
        "Respond whether the answer is correct or not, and justify your judgment in 1–2 lines.\n\n"
        f"QUESTION:\n{question}\n\n"
        f"ANSWER:\n{user_answer}"
    )

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=300,
            top_p=1
        )

        return response.choices[0].message.content.strip()

    except Exception as e:

        return f"❌ Evaluation error: {e}"
