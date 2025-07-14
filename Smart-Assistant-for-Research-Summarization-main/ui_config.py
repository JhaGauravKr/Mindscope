import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
        :root {
            --primary: #6e48aa;
            --secondary: #9d50bb;
            --accent: #4776e6;
            --light: #f8f9fa;
            --dark: #1c1f26;
            --card-dark: #2b2f36;
            --glass: rgba(43, 47, 54, 0.75);
            --glow: 0 0 20px rgba(110, 72, 170, 0.6);
        }

        html, body, .stApp {
            background-color: var(--dark);
            color: white;
        }

        .hero-header {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            box-shadow: var(--glow);
        }

        .hero-header h1 {
            font-size: 3rem;
            margin-bottom: 0.3rem;
        }

        .tagline {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        .card {
            background: var(--glass);
            border-radius: 14px;
            padding: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            backdrop-filter: blur(12px);
            margin-bottom: 1.5rem;
            color: white;
            animation: fadeIn 0.5s ease-in-out;
        }

        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            background-color: var(--card-dark) !important;
            color: white !important;
            border-radius: 10px;
            padding: 10px;
            border: 1px solid var(--secondary);
        }

        .stButton > button {
            background: linear-gradient(135deg, var(--primary), var(--secondary)) !important;
            color: white;
            border: none;
            padding: 0.6rem 1.5rem;
            border-radius: 10px;
            font-weight: bold;
            box-shadow: 0 0 10px rgba(157, 80, 187, 0.5);
        }

        .stButton > button:hover {
            transform: scale(1.03);
            box-shadow: 0 0 20px rgba(157, 80, 187, 0.7);
        }

        .footer {
            text-align: center;
            padding: 1.5rem 0 0;
            font-size: 0.9rem;
            color: #aaa;
            opacity: 0.85;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(15px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
    """, unsafe_allow_html=True)


