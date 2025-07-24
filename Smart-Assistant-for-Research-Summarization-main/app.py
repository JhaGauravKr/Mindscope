import os
import streamlit as st
from dotenv import load_dotenv

# ───── Load API Key ─────
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
if not groq_api_key:
    st.error("❌ GROQ_API_KEY is not set. Please add it to your .env file.")
    st.stop()

from utils.pdf_reader import extract_text
from utils.summarizer import summarise_document
from utils.qa_engine import answer_question
from utils.challenge import (
    generate_subjective_questions,
    evaluate_subjective
)
from utils.mindmap import generate_mindmap
from ui_config import inject_custom_css, show_sidebar_info, hero_header

# ───── Streamlit Config ─────
st.set_page_config("🧠 MindScope: AI-Powered Research Assistant", layout="wide")
inject_custom_css()
show_sidebar_info()
hero_header()


def main():
    # ───── Upload Document ─────
    uploaded_file = st.file_uploader("📤 Upload Research Document (PDF or TXT)", type=["pdf", "txt"])

    if uploaded_file:
        with st.spinner("🔍 Extracting document text..."):
            doc_text = extract_text(uploaded_file)

        if not doc_text.strip():
            st.error("⚠️ No readable text found. Try another file.")
            return

        st.success("✅ Document successfully parsed.")
        st.session_state["doc_text"] = doc_text

        # ───── Mind Map ─────
        st.subheader("🧠 Mind Map")
        with st.spinner("Generating conceptual map..."):
            try:
                mindmap = generate_mindmap(doc_text)
                st.graphviz_chart(mindmap)

            except Exception as e:
                st.error(f"❌ Mind map error: {e}")

        # ───── Summary ─────
        st.subheader("📄 Executive Summary")
        if "summary" not in st.session_state:
            with st.spinner("Summarizing document..."):
                try:
                    summary = summarise_document(doc_text, groq_api_key)
                    st.session_state["summary"] = summary
                except Exception as e:
                    st.error(f"❌ Error summarizing: {e}")
                    return

        st.markdown(st.session_state["summary"])

        # ───── Q&A ─────
        st.subheader("💬 Ask a Question")
        question = st.text_input("Ask a question about this document:")
        if question:
            with st.spinner("Generating answer..."):
                try:
                    result = answer_question(doc_text, question, groq_api_key)
                    st.markdown(f"**✅ Answer:** {result['answer']}")
                    if result.get("justification"):
                        st.markdown(f"**📚 Justification:** {result['justification']}")
                except Exception as e:
                    st.error(f"❌ Q&A error: {e}")

       # ───── Challenge Mode ─────
        st.subheader("🎯 Challenge Yourself")
        if st.button("🧠 Generate Subjective Questions"):
            with st.spinner("Creating challenge..."):
                try:
                    st.session_state["subjective"] = generate_subjective_questions(doc_text, groq_api_key)
                    st.success("✅ Subjective questions generated.")
                except Exception as e:
                    st.error(f"❌ Error generating questions: {e}")

        # ───── Subjective Evaluation ─────
        if "subjective" in st.session_state:
            st.markdown("### ✍️ Subjective Questions")
            for i, q in enumerate(st.session_state["subjective"], 1):
                user_answer = st.text_area(f"Q{i}: {q}", key=f"sub_q{i}")
                if st.button(f"Evaluate Q{i}", key=f"eval_sub_q{i}"):
                    with st.spinner("Evaluating your response..."):
                        feedback = evaluate_subjective(user_answer, q, groq_api_key)
                        st.info(f"📋 **Feedback:** {feedback}")

    else:
        st.info("📥 Please upload a PDF or TXT file to begin.")

# ───── Main Entrypoint ─────
if __name__ == "__main__":
    main()
