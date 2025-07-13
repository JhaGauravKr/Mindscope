import streamlit as st
import numpy as np
import pandas as pd
from graphviz import Digraph
from sklearn.feature_extraction.text import TfidfVectorizer
from utils.pdf_reader import extract_text_from_pdf
from utils.summarizer import summarize_text
from utils.qa_engine import ask_question_from_doc, generate_logic_questions, evaluate_user_answer
from ui_config import inject_custom_css

st.set_page_config(
    page_title="NeuroScholar | Smart Assistant for Research Summarization",
    layout="wide",
    page_icon="🧠",
    initial_sidebar_state="expanded"
)

inject_custom_css()


with st.sidebar:
    st.title("🧠 About")

    st.markdown("""
    **MindScope** is a privacy-focused, AI-powered research assistant that helps users summarize academic content, visualize key ideas through mind maps, and interact with intelligent question-answering modules — all locally on your device.

    ---
    **👤 Author:** [Gaurav Kumar Jha](https://www.linkedin.com/in/gaurav-kumar-jha-525063276)  
    **📧 Email:** [jhagauravkumar20@gmail.com](mailto:jhagauravkumar20@gmail.com)  
    **🔗 GitHub:** [@jhagauravkr](https://github.com/jhagauravkr)
    """)

def create_mind_map(text, max_terms=10):
    try:
        vectorizer = TfidfVectorizer(max_features=50, stop_words='english')
        X = vectorizer.fit_transform([text])
        terms = vectorizer.get_feature_names_out()
        scores = np.asarray(X.sum(axis=0)).flatten()

        sorted_indices = scores.argsort()[::-1]
        top_terms = terms[sorted_indices[:max_terms]]

        dot = Digraph()
        root = top_terms[0]
        dot.node(root, root, shape='ellipse', style='filled', color='lightblue')

        children = top_terms[1:6]
        for child in children:
            dot.node(child, child)
            dot.edge(root, child)

        for parent in children:
            second_level = np.random.choice(
                [t for t in top_terms if t != parent and t != root],
                size=2, replace=False
            )
            for sub in second_level:
                dot.node(sub, sub)
                dot.edge(parent, sub)

        return dot

    except Exception as e:
        st.error(f"❌ Failed to generate mind map: {str(e)}")
        return None

def main():
    st.markdown("""
    <div class="hero-header">
        <h1>🧠 MindScope</h1>
            <p class="tagline">Your AI-Powered Research Insight Generator.</p>
    </div>
    """, unsafe_allow_html=True)


    uploaded_file = st.file_uploader("📤 Upload Research Document (PDF or TXT)", type=["pdf", "txt"])

    if uploaded_file:
        if "uploaded_file_name" not in st.session_state or st.session_state.uploaded_file_name != uploaded_file.name:
            st.session_state.raw_text = None
            st.session_state.summary = None
            st.session_state.questions = None
            st.session_state.qa_history = []
            st.session_state.uploaded_file_name = uploaded_file.name



        if st.session_state.raw_text is None:
            if uploaded_file.type == "application/pdf":
                st.session_state.raw_text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.type == "text/plain":
                st.session_state.raw_text = uploaded_file.read().decode("utf-8")

        with st.expander("📄 Raw Text Preview (Debug)", expanded=False):
            st.text_area("First 1000 characters", st.session_state.raw_text[:1000])

        if st.session_state.raw_text:
            with st.expander("🧠 Document Mind Map", expanded=True):
                mind_map = create_mind_map(st.session_state.raw_text)
                if mind_map:
                    st.graphviz_chart(mind_map)
                else:
                    st.warning("Unable to generate mind map.")

            if st.session_state.summary is None:
                with st.spinner("Generating intelligent summary..."):
                    st.session_state.summary = summarize_text(st.session_state.raw_text)

            with st.expander("Executive Summary", expanded=True):
                word_count = len(st.session_state.summary.split())
                st.markdown(f"""
                <div class="card fade-in">
                    <div style="font-size: 0.9rem; color: #ccc; margin-bottom: 10px;">
                        {word_count} words | Key Insights
                    </div>
                    <div style="line-height: 1.6;">
                        {st.session_state.summary}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            mode = st.radio("Choose Mode", ["Ask Questions", "Test Knowledge"], horizontal=True)

            if mode == "Ask Questions":
                if "qa_history" not in st.session_state:
                    st.session_state.qa_history = []

                user_question = st.text_input("Ask a question:")

                if user_question:
                    with st.spinner("Answering..."):
                        answer = ask_question_from_doc(user_question, st.session_state.raw_text)
                        st.success(f"**Answer:** {answer}")
                        st.session_state.qa_history.append((user_question, answer))

                if st.session_state.qa_history:
                    st.markdown("### 🧾 Conversation History")

                    # Optional clear button
                    if st.button("🧹 Clear Conversation History"):
                        st.session_state.qa_history = []

                    with st.container():
                        for i, (q, a) in enumerate(reversed(st.session_state.qa_history), 1):
                            st.markdown(f"""
                                <div class="card fade-in" style="background-color: var(--card-dark); margin-bottom: 1rem;">
                                    <div><strong>Q{i}:</strong> {q}</div>
                                    <div style="margin-top: 5px;"><strong>A:</strong> {a}</div>
                                </div>
                                """, unsafe_allow_html=True)

            
            else:
                    if "questions" not in st.session_state:
                        st.session_state.questions = []

                    if st.button("🔄 Generate Questions"):
                        with st.spinner("Generating questions from the document..."):
                            questions = generate_logic_questions(st.session_state.raw_text)
                            if questions and isinstance(questions, list):
                                st.session_state.questions = questions
                            else:
                                st.session_state.questions = [
                                    "What is the main idea of the document?",
                                    "What problem is the research trying to solve?",
                                    "What is the conclusion or result mentioned?"
                                ]

                    if st.session_state.questions:
                        with st.form("qa_form"):
                            user_answers = {}
                            for i, q in enumerate(st.session_state.questions):
                                key = f"user_answer_{i}_{hash(q)}"  # ✅ Unique key even if text repeats
                                user_answers[q] = st.text_area(f"Q{i+1}: {q}", key=key)

                            submitted = st.form_submit_button("Submit Answers")

                        if submitted:
                            for q, user_ans in user_answers.items():
                                if user_ans.strip():
                                    with st.spinner(f"Evaluating: {q[:60]}..."):
                                        feedback = evaluate_user_answer(st.session_state.raw_text, q, user_ans)

                                    if "excellent" in feedback.lower():
                                        st.success("✅ Excellent\n\n" + feedback)
                                    elif "good" in feedback.lower():
                                        st.info("🟡 Good\n\n" + feedback)
                                    elif "almost" in feedback.lower():
                                        st.warning("🔍 Almost There\n\n" + feedback)
                                    else:
                                        st.error("❌ Needs Improvement\n\n" + feedback)


    else:
        st.markdown("""
<div class="card" style="text-align: center;">
    <h2>📄 Welcome to <span style="color:#9d50bb;">MindScope</span></h2>
<p style="font-size: 1.1rem;">
Upload a research paper to unlock summaries, mind maps, and interactive Q&A insights.<br>
<small>We do not store or share your data.</small>
</p>
</div>
""", unsafe_allow_html=True)



    st.markdown("""
    <div class="footer">
        MindScope | © 2025 Gaurav Kumar Jha
    </div>
""", unsafe_allow_html=True)


if __name__ == "__main__":
    main()