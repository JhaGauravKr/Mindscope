# import streamlit as st

# def inject_custom_css():
#     st.set_page_config(
#     page_title="NeuroScholar | Smart Assistant for Research Summarization",
#     layout="wide",
#     page_icon="🧠",
#     initial_sidebar_state="expanded"
# )

# st.markdown("""
# <style>
#     :root {
#         --primary: #6e48aa;
#         --secondary: #9d50bb;
#         --accent: #4776e6;
#         --light: #f8f9fa;
#         --dark: #f8f9fa;
#         --card-dark: #2b2f36;
#     }

#     .main {
#         background: linear-gradient(135deg, #f5f7fa 0%, #e4e8eb 100%);
#     }

#     .stApp {
#         background: transparent;
#     }

#     .stTextInput>div>div>input, .stTextArea>div>div>textarea {
#         border-radius: 12px !important;
#         padding: 12px !important;
#         box-shadow: 0 2px 10px rgba(0,0,0,0.05) !important;
#         background-color: var(--card-dark) !important;
#         color: white !important;
#     }

#     .stButton>button {
#         background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
#         color: white !important;
#         border-radius: 12px !important;
#         padding: 10px 24px !important;
#         font-weight: 500 !important;
#         border: none !important;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1) !important;
#         transition: all 0.3s !important;
#     }

#     .stButton>button:hover {
#         transform: translateY(-2px) !important;
#         box-shadow: 0 6px 12px rgba(0,0,0,0.15) !important;
#     }

#     .stRadio>div {
#         gap: 10px;
#     }

#     .stRadio>div>label {
#         border-radius: 12px !important;
#         padding: 10px 20px !important;
#         background: var(--card-dark) !important;
#         color: white !important;
#         box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important;
#         transition: all 0.3s !important;
#     }

#     .stRadio>div>label:hover {
#         box-shadow: 0 4px 12px rgba(0,0,0,0.15) !important;
#     }

#     .stRadio>div>label[data-baseweb="radio"]>div:first-child {
#         border-color: var(--primary) !important;
#     }

#     .stRadio>div>label[data-baseweb="radio"]>div:first-child>div {
#         background-color: var(--primary) !important;
#     }

#     .stExpander {
#         background: var(--card-dark) !important;
#         color: white !important;
#         border-radius: 12px !important;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
#         border: none !important;
#     }

#     .stExpander .streamlit-expanderHeader {
#         font-weight: 600 !important;
#         color: var(--light) !important;
#     }

#     .card {
#         background: var(--card-dark) !important;
#         border-radius: 12px;
#         padding: 20px;
#         color: white;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.08);
#         margin-bottom: 20px;
#     }

#     .gradient-header {
#         background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
#         color: white;
#         padding: 20px;
#         border-radius: 12px;
#         margin-bottom: 20px;
#         box-shadow: 0 4px 12px rgba(0,0,0,0.15);
#     }

#     @keyframes fadeIn {
#         from { opacity: 0; transform: translateY(10px); }
#         to { opacity: 1; transform: translateY(0); }
#     }

#     .fade-in {
#         animation: fadeIn 0.5s ease-out forwards;
#     }
# </style>
# """, unsafe_allow_html=True)

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


