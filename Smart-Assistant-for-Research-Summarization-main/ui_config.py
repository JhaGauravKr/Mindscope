# ui_config.py

import streamlit as st

def set_custom_page_config():
    st.set_page_config(
        page_title="MindScope | AI-Powered Research Insight Generator",
        layout="wide",
        page_icon="🧠",
        initial_sidebar_state="expanded"
    )

def inject_custom_css():
    st.markdown("""
    <style>
    body {
        background-color: #f9fafb;
    }

    h1, h2, h3 {
        color: #1f2937;
    }

    .stButton>button {
        border-radius: 8px;
        background: linear-gradient(135deg, #4f46e5, #6366f1);
        color: #ffffff;
        font-weight: 600;
        border: none;
        padding: 0.6em 1.4em;
        box-shadow: 0 4px 12px rgba(79,70,229,0.3);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(135deg, #4338ca, #4f46e5);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(67,56,202,0.4);
    }

    .stFileUploader {
        border: 2px dashed #4f46e5;
        border-radius: 12px;
        padding: 1em;
        background-color: #000000;
        color: #ffffff;
    }

    .stTextInput>div>div>input {
        border-radius: 6px;
        border: 1px solid #d1d5db;
        padding: 0.4em;
        background-color: #111111;
        color: #ffffff;
    }

    .stRadio>div {
        background-color: #111111;
        border-radius: 10px;
        padding: 1em;
        color: #ffffff;
    }

    .stExpander {
        border-radius: 10px;
        background-color: #111111;
        border: 1px solid #333333;
        color: #ffffff;
    }

    .stExpanderSummary {
        font-weight: 600;
    }

    .stSpinner {
        color: #4f46e5 !important;
    }

    .stMarkdown {
        background-color: #111111;
        color: #ffffff;
        border-radius: 8px;
        padding: 1em;
    }
    </style>
    """, unsafe_allow_html=True)

def show_sidebar_info():
    with st.sidebar:
        st.title("🧠 About")

        st.markdown("""
    **MindScope** is a privacy-focused, AI-powered research assistant that helps users summarize academic content, visualize key ideas through mind maps, and interact with intelligent question-answering modules — all locally on your device.

    ---
    **👤 Author:** [Gaurav Kumar Jha](https://www.linkedin.com/in/gaurav-kumar-jha-525063276)  
    **📧 Email:** [jhagauravkumar20@gmail.com](mailto:jhagauravkumar20@gmail.com)  
    **🔗 GitHub:** [@jhagauravkr](https://github.com/jhagauravkr)
    """)

def hero_header():
    st.markdown("""
    <div class="hero-header">
        <h1>🧠 MindScope</h1>
        <p class="tagline">Your AI-Powered Research Insight Generator.</p>
    </div>
    """, unsafe_allow_html=True)

def footer():
    st.markdown("""
    <div class="footer" style="text-align: center; margin-top: 50px;">
        <small>MindScope | © 2025 Gaurav Kumar Jha</small>
    </div>
    """, unsafe_allow_html=True)
