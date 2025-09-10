from groq import Groq

def answer_question(document_text: str, question: str, api_key: str) -> dict:
    """
    Use Groq + LLaMA 3 to answer a question from the document.
    Returns both the answer and a justification if found.
    """
    try:
        client = Groq(api_key=api_key)

        prompt = (
            "You are a helpful research assistant. Answer the question **only** using the content from the document below.\n\n"
            f"DOCUMENT:\n{document_text[:10000]}\n\n"
            f"QUESTION:\n{question}\n\n"
            "Then provide a 'Justification:' section by quoting a relevant line or explanation."
        )

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=512,
            top_p=1
        )

        content = response.choices[0].message.content.strip()

        # Split answer and justification
        if "Justification:" in content:
            answer, justification = content.split("Justification:", 1)
            return {
                "answer": answer.strip(),
                "justification": justification.strip()
            }

        return {"answer": content, "justification": ""}

    except Exception as e:

        raise RuntimeError(f"Q&A error: {str(e)}")
