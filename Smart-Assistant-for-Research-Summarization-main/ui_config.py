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

    /* DARK THEME */
    [data-theme="dark"] {
        background-color: #0f172a;
        color: #f8fafc;
    }

    [data-theme="dark"] .stMarkdown {
        background-color: #1e293b;
        color: #f8fafc;
    }

    /* LIGHT THEME */
    [data-theme="light"] {
        background-color: #ffffff;
        color: #111827;
    }

    [data-theme="light"] .stMarkdown {
        background-color: #f3f4f6;
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

    .hero-header h1 {
        font-size: 3rem;
        font-weight: bold;
    }

    .hero-header p {
        font-size: 1.2rem;
        margin-top: -1rem;
        color: #6b7280;
    }
    </style>
    """, unsafe_allow_html=True)


def theme_toggle():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown('<div class="top-bar"><button class="about-button" onclick="window.showAbout=true">About</button>', unsafe_allow_html=True)
    with col2:
        toggle = st.button("🌙 Toggle Theme", key="theme_toggle")
        if toggle:
            st.session_state.dark_mode = not st.session_state.dark_mode

    st.markdown('</div>', unsafe_allow_html=True)

    # Set light/dark mode CSS dynamically
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        body, .stApp {
            background-color: #111827;
            color: #ffffff;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            background-color: #1f2937;
            color: #ffffff;
            border: 1px solid #374151;
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
        body, .stApp {
            background-color: #f9fafb;
            color: #1f2937;
        }
        .stTextInput>div>div>input, .stTextArea>div>textarea {
            background-color: #ffffff;
            color: #000000;
            border: 1px solid #d1d5db;
        }
        .stButton>button {
            background: linear-gradient(135deg, #4f46e5, #6366f1);
            color: white;
        }
        </style>
        """, unsafe_allow_html=True)


def about_modal():
    if "show_about" not in st.session_state:
        st.session_state.show_about = False

    with st.container():
        cols = st.columns([8, 2])
        with cols[0]:
            if st.button("About", key="about_button"):
                st.session_state.show_about = not st.session_state.show_about

        if st.session_state.show_about:
            st.markdown("""
            <div class="about-content" style="background-color: #f0f4f8; padding: 1em; border-radius: 10px;">
                <h4>🧠 About MindScope</h4>
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
            </div>
            """, unsafe_allow_html=True)

def hero_header():
    st.markdown("""
    <div style="margin-top:20px; margin-bottom:30px;">
        <h1 style="font-size: 3rem;">🧠 MindScope</h1>
        <p style="font-size: 1.2rem; color: #6b7280;">Your AI-Powered Research Insight Generator</p>
    </div>
    """, unsafe_allow_html=True)

def show_sidebar_info():
    pass  # About is now in top bar modal

def footer():
    st.markdown("""
    <div style="text-align: center; margin-top: 4rem;">
        <small style="color: gray;">MindScope | © 2025 Gaurav Kumar Jha</small>
    </div>
    """, unsafe_allow_html=True)
