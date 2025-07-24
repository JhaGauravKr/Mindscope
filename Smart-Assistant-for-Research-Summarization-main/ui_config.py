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

    /* THEME-SPECIFIC GLOBAL STYLES (via data-theme attribute) */
    [data-theme="dark"] {
        background-color: #0f172a;
        color: #f8fafc; /* General text color for dark theme */
    }

    [data-theme="dark"] .stMarkdown {
        background-color: #1e293b; /* Slightly lighter background for markdown blocks */
        color: #f8fafc;
    }

    [data-theme="light"] {
        background-color: #ffffff;
        color: #111827; /* General text color for light theme */
    }

    [data-theme="light"] .stMarkdown {
        background-color: #f3f4f6; /* Slightly darker background for markdown blocks */
        color: #111827;
    }

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

    /* Upload area */
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
        color: #6b7280;
    }

    /* Streamlit Alert Boxes: Info and Success */
    /* Light theme info */
    .stAlert.info {
        background-color: #e0f2fe; /* Light blue */
        color: #0c4a6e; /* Dark blue text */
    }
    /* Dark theme info */
    [data-theme="dark"] .stAlert.info {
        background-color: #1e3a8a; /* Darker blue */
        color: #bfdbfe; /* Lighter blue text */
    }

    /* Light theme success */
    .stAlert.success {
        background-color: #dcfce7; /* Light green */
        color: #166534; /* Dark green text */
    }
    /* Dark theme success */
    [data-theme="dark"] .stAlert.success {
        background-color: #166534; /* Darker green */
        color: #bbf7d0; /* Lighter green text */
    }

    /* About Expander Content Specific Styles (if using expander) */
    .st-expander { /* Target the expander component itself */
        background-color: var(--background-color, #f0f4f8); /* Use CSS variable for background */
        border-radius: 10px;
        padding: 1em; /* Add some padding inside the expander */
        border: 1px solid var(--border-color, #d1d5db);
    }
    .st-expander details { /* Target the details tag inside the expander */
        padding: 0; /* Remove default padding from details */
    }
    .st-expander details summary { /* Target the summary (header) of the expander */
        color: var(--text-color, #111827); /* Ensure header text is visible */
    }
    .st-expander details div { /* Target the content div inside the expander */
        color: var(--text-color, #111827); /* Ensure content text is visible */
    }

    /* Ensure general text elements are visible */
    /* This targets various text-displaying components in Streamlit */
    .stText, .stMarkdown, .stLabel, .stTextInput>div>label, .stTextArea>label {
        color: var(--text-color, #111827); /* Fallback for good measure */
    }

    /* Input and TextArea specific styling (dynamic in theme_toggle) */
    .stTextInput>div>div>input, .stTextArea>div>textarea {
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

    # Set dynamic CSS variables for theme
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        :root {
            --text-color: #f8fafc;
            --background-color: #111827;
            --border-color: #374151;
            --input-background-color: #1f2937;
            --input-text-color: #ffffff;
            --input-border-color: #374151;
        }
        body, .stApp {
            background-color: var(--background-color);
            color: var(--text-color); /* Apply general text color */
        }
        .stButton>button {
            background: #4f46e5;
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        :root {
            --text-color: #111827;
            --background-color: #f9fafb;
            --border-color: #d1d5db;
            --input-background-color: #ffffff;
            --input-text-color: #000000;
            --input-border-color: #d1d5db;
        }
        body, .stApp {
            background-color: var(--background-color);
            color: var(--text-color); /* Apply general text color */
        }
        .stButton>button {
            background: linear-gradient(135deg, #4f46e5, #6366f1);
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)


def about_section(): # Renamed to reflect it's now an expander, not a modal
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
