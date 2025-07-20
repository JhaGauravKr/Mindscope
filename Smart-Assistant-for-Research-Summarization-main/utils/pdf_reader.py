from PyPDF2 import PdfReader
from io import StringIO
import streamlit as st

def extract_text(file) -> str:
    """Extract plain text from uploaded PDF or TXT file."""
    file_type = getattr(file, "type", "").lower()

    if file_type == "application/pdf":
        try:
            reader = PdfReader(file)
            return "\n".join((page.extract_text() or "") for page in reader.pages)
        except Exception as e:
            st.error(f"❌ Error reading PDF: {e}")
            return ""

    elif file_type == "text/plain":
        try:
            return StringIO(file.getvalue().decode("utf-8", "ignore")).read()
        except Exception as e:
            st.error(f"❌ Error reading TXT file: {e}")
            return ""

    st.error("❌ Unsupported file format. Please upload a PDF or TXT file.")
    return ""
