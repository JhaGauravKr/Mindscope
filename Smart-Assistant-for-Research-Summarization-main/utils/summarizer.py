
from groq import Groq

def summarise_document(text: str, api_key: str) -> str:
    """
    Summarizes the given academic text using LLaMA 3 via Groq API.
    Limits output to ~150 words.
    """
    try:
        client = Groq(api_key=api_key)

        prompt = (
            "You are an academic assistant. Summarize the following document in 120 to 150 words. "
            "The summary should cover the main ideas, purpose, and conclusions without adding extra information.\n\n"
            f"Document:\n{text[:10000]}"
        )

        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            # model="llama3-70b-8192",  # ✅ Updated to a supported model
            model="llama-3.3-70b-versatile",
            temperature=0.4,
            max_tokens=400,
            top_p=1
        )

        summary = response.choices[0].message.content.strip()
        return summary

    except Exception as e:

        raise RuntimeError(f"Summarization error: {str(e)}")

