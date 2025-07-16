from transformers import pipeline, BartTokenizer
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")

def summarize_text(text, min_words=80, max_words=150):
    tokens = tokenizer.encode(text, truncation=True, max_length=1024)
    trimmed_text = tokenizer.decode(tokens, skip_special_tokens=True)

    summary = summarizer(
        trimmed_text,
        max_length=300,   # ~150 words
        min_length=120,   # ~80 words
        do_sample=False,
        truncation=True
    )[0]['summary_text']

    # 3. Final word count enforcement
    words = word_tokenize(summary)
    word_count = len(words)

    if word_count > max_words:
        summary = " ".join(words[:max_words]) + "..."
    elif word_count < min_words:
        summary += " (Note: Summary is short — consider uploading a longer or more content-rich document.)"

    return summary