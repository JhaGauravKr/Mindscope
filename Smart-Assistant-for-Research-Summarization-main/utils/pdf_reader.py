import fitz

def extract_text_from_pdf(file):
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text("text")  # Use "text" mode
        return text if text.strip() else "⚠️ No extractable text found."
    except Exception as e:
        return f"Error reading PDF: {e}"

def extract_text_from_txt(file):
    try:
        text = file.read()
        return text.decode("utf-8") if isinstance(text, bytes) else text
    except Exception as e:
        return f"Error reading TXT: {e}"

def extract_text(file, file_type):
    if file_type.lower() == "pdf":
        return extract_text_from_pdf(file)
    elif file_type.lower() == "txt":
        return extract_text_from_txt(file)
    return "Unsupported file type."
