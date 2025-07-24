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
    body {
        font-family: 'Segoe UI', sans-serif;
        transition: background-color 0.5s ease, color 0.5s ease;
    }

    .top-bar {
        position: sticky;
        top: 0;
        background-color: #1f2937;
        color: white;
        z-index: 999;
        padding: 0.8rem 1.2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 0 0 10px 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }

    .about-button {
        background: none;
        color: white;
        border: 1px solid white;
        padding: 0.4rem 1rem;
        border-radius: 6px;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .about-button:hover {
        background-color: #4f46e5;
        color: #fff;
        border-color: #4f46e5;
    }

    .theme-toggle {
        font-size: 0.9rem;
        padding: 0.4rem 0.8rem;
        background-color: #6366f1;
        border: none;
        border-radius: 6px;
        color: white;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .theme-toggle:hover {
        background-color: #4338ca;
    }

    .animated-upload {
        animation: pulse 1.5s infinite;
    }

    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(79,70,229, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(79,70,229, 0); }
        100% { box-shadow: 0 0 0 0 rgba(79,70,229, 0); }
    }

    .stFileUploader {
        border: 2px dashed #4f46e5;
        border-radius: 10px;
        padding: 1rem;
        background-color: #f9fafb;
        text-align: center;
    }

    .stMarkdown, .stTextInput, .stTextArea, .stSelectbox, .stButton>button {
        border-radius: 8px;
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
    st.markdown("""
    <script>
    const aboutPopup = () => {
        const html = `<div id="about-modal" style="
            position: fixed; top: 20%; left: 50%; transform: translate(-50%, -20%);
            background-color: #1f2937; color: white; padding: 2rem; border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3); z-index: 9999;
            max-width: 600px; text-align: left;">
            <h3>About MindScope</h3>
            <p><b>MindScope</b> is a privacy-focused AI-powered assistant that summarizes research documents, generates mind maps, answers questions, and evaluates understanding through intelligent challenges.</p>
            <hr style="border-top: 1px solid #555;">
            <p><b>👤 Author:</b> Gaurav Kumar Jha</p>
            <p><b>📧 Email:</b> jhagauravkumar20@gmail.com</p>
            <p><b>🔗 GitHub:</b> <a href='https://github.com/jhagauravkr' target='_blank' style='color: #60a5fa;'>@jhagauravkr</a></p>
            <p><b>🚀 Deployed:</b> <a href='https://jhagauravkr-mindscope.streamlit.app/' target='_blank' style='color: #60a5fa;'>Click Here</a></p>
            <div style="margin-top: 1rem; text-align: right;">
                <button onclick="document.getElementById('about-modal').remove()" style="
                    background-color: #4f46e5; color: white; padding: 0.5rem 1rem;
                    border: none; border-radius: 6px; cursor: pointer;">Close</button>
            </div>
        </div>`;
        if (!window.showAbout) return;
        document.body.insertAdjacentHTML('beforeend', html);
        window.showAbout = false;
    };
    setInterval(aboutPopup, 500);
    </script>
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
