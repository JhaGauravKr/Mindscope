import streamlit as st

def set_custom_page_config():
    st.set_page_config(
        page_title="MindScope | AI-Powered Research Insight Generator",
        layout="wide",
        page_icon="🧠",
        initial_sidebar_state="collapsed"
    )

def inject_custom_css():
    st.markdown("""
    <style>
    /* GLOBAL RESET */
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    /* Streamlit's data-theme is handled by theme_toggle now via :root variables */

    /* Buttons */
    .stButton>button {
        border-radius: 8px;
        padding: 0.6em 1.4em;
        font-weight: 600;
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    }

    /* Upload area container styling */
    .stFileUploader {
        border: 2px dashed #6366f1;
        border-radius: 12px;
        padding: 1em;
    }

    /* Hero Header */
    .hero-header h1 {
        font-size: 3rem;
        font-weight: bold;
    }

    .hero-header p {
        font-size: 1.2rem;
        margin-top: -1rem;
        color: #6b7280; /* This can remain a fixed neutral color */
    }

    /* Streamlit Alert Boxes: Info and Success */
    /* Light theme info */
    .stAlert.info {
        background-color: #e0f2fe; /* Light blue */
        color: #0c4a6e; /* Direct text color for info alerts in light theme */
    }
    /* Dark theme info */
    [data-theme="dark"] .stAlert.info {
        background-color: #1e3a8a; /* Darker blue */
        color: #bfdbfe; /* Direct text color for info alerts in dark theme */
    }

    /* Light theme success */
    .stAlert.success {
        background-color: #dcfce7; /* Light green */
        color: #166534; /* Direct text color for success alerts in light theme */
    }
    /* Dark theme success */
    [data-theme="dark"] .stAlert.success {
        background-color: #166534; /* Darker green */
        color: #bbf7d0; /* Direct text color for success alerts in dark theme */
    }

    /* About Expander Content Specific Styles */
    .st-expander {
        background-color: var(--background-color-secondary); /* Use a secondary background variable */
        border-radius: 10px;
        padding: 1em;
        border: 1px solid var(--border-color);
    }
    .st-expander details summary,
    .st-expander details div {
        color: var(--text-color); /* Ensure text is visible inside expander */
    }

    /* Universal text color for various Streamlit elements */
    /* This targets a wide range of text-displaying components */
    .stText,
    .stMarkdown,
    .stLabel,
    .stBlock, /* General block elements, often contain text */
    .stFileUploader label, /* Label "Upload Research Document" */
    .stFileUploader > div > button + div, /* "Drag and drop file here" and "Limit 200MB" */
    .stTextInput>div>label,
    .stTextArea>label,
    .stSelectbox>label,
    .stRadio>label,
    .stCheckbox>label {
        color: var(--text-color) !important; /* Apply global text color, !important as a last resort */
    }

    /* Input and TextArea specific styling */
    .stTextInput>div>div>input,
    .stTextArea>div>textarea {
        background-color: var(--input-background-color);
        color: var(--input-text-color);
        border: 1px solid var(--input-border-color);
    }

    </style>
    """, unsafe_allow_html=True)


def theme_toggle():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    toggle = st.button("🌙 Toggle Theme", key="theme_toggle")
    if toggle:
        st.session_state.dark_mode = not st.session_state.dark_mode

    # Set dynamic CSS variables for theme on :root
    # These variables will then be used by other CSS rules
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        :root {
            --text-color: #f8fafc; /* Very light gray */
            --background-color: #0f172a; /* Dark blue-gray for main app background */
            --background-color-secondary: #1e293b; /* Slightly lighter dark for components like expanders */
            --border-color: #374151; /* Darker border */
            --input-background-color: #1f2937;
            --input-text-color: #ffffff;
            --input-border-color: #374151;
        }
        body, .stApp {
            background-color: var(--background-color);
            color: var(--text-color); /* Apply general text color to body/app */
        }
        .stButton>button {
            background: #4f46e5; /* Primary button color */
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        :root {
            --text-color: #111827; /* Very dark gray */
            --background-color: #ffffff; /* White for main app background */
            --background-color-secondary: #f3f4f6; /* Lighter gray for components like expanders */
            --border-color: #d1d5db; /* Light border */
            --input-background-color: #ffffff;
            --input-text-color: #000000;
            --input-border-color: #d1d5db;
        }
        body, .stApp {
            background-color: var(--background-color);
            color: var(--text-color); /* Apply general text color to body/app */
        }
        .stButton>button {
            background: linear-gradient(135deg, #4f46e5, #6366f1); /* Gradient for light theme buttons */
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)


def about_section():
    with st.expander("About MindScope 🧠"):
        st.markdown("""
            <p>
                <b>MindScope</b> is a privacy-focused, AI-powered research assistant that helps users:
                <ul>
                    <li>📄 Summarize academic content</li>
                    <li>🧠 Generate mind maps</li>
                    <li>💬 Interact with intelligent Q&A modules</li>
                    <li>🎯 Practice subjective questions with AI evaluation</li>
                </ul>
            </p>
            <hr/>
            <b>👨‍💻 Author:</b> <a href="https://www.linkedin.com/in/gaurav-kumar-jha-525063276" target="_blank">Gaurav Kumar Jha</a><br/>
            <b>📧 Email:</b> <a href="mailto:jhagauravkumar20@gmail.com">jhagauravkumar20@gmail.com</a><br/>
            <b>🔗 GitHub:</b> <a href="https://github.com/jhagauravkr" target="_blank">@jhagauravkr</a>
        """, unsafe_allow_html=True)


def hero_header():
    st.markdown("""
    <div style="margin-top:20px; margin-bottom:30px;">
        <h1 style="font-size: 3rem;">🧠 MindScope</h1>
        <p style="font-size: 1.2rem; color: #6b7280;">Your AI-Powered Research Insight Generator</p>
    </div>
    """, unsafe_allow_html=True)

def show_sidebar_info():
    pass

def footer():
    st.markdown("""
    <div style="text-align: center; margin-top: 4rem;">
        <small style="color: gray;">MindScope | © 2025 Gaurav Kumar Jha</small>
    </div>
    """, unsafe_allow_html=True)
