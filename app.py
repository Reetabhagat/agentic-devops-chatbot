import streamlit as st
from main import controller_agent
import base64

st.set_page_config(page_title="Agentic DevOps Chatbot", layout="wide")

# ---------------- BACKGROUND ---------------- #

def add_bg_from_local(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}

        .chat-box {{
            background: rgba(0,0,0,0.6);
            padding: 20px;
            border-radius: 15px;
        }}

        .user-msg {{
            background-color: #1f77ff;
            padding: 12px;
            border-radius: 12px;
            margin: 8px 0;
            color: white;
            text-align: right;
        }}

        .bot-msg {{
            background-color: #2e2e2e;
            padding: 12px;
            border-radius: 12px;
            margin: 8px 0;
            color: white;
            text-align: left;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("assets/bg.jpg")

# ---------------- HEADER ---------------- #

st.markdown("""
<div style="text-align:center; padding:30px;">
<h1 style="font-size:50px; font-weight:800; color:white;">
🤖 Agentic DevOps Chatbot
</h1>
<p style="font-size:18px; color:white;">
AI-powered DevOps assistant that thinks like a Senior Cloud Engineer
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ---------------- #

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- DOMAIN BUTTONS ---------------- #

st.markdown("### 🔥 Choose Your Domain")

domains = [
    "AWS", "Terraform", "CI/CD", "Kubernetes",
    "Docker", "Git", "GitHub", "Linux",
    "Monitoring", "Helm"
]

cols = st.columns(5)

for i, domain in enumerate(domains):
    if cols[i % 5].button(domain):
        st.session_state.chat_history.append(
            ("user", f"Show {domain} related examples")
        )
        response = controller_agent(domain.lower())
        st.session_state.chat_history.append(("bot", response))

# ---------------- CHAT DISPLAY ---------------- #

st.markdown('<div class="chat-box">', unsafe_allow_html=True)

for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(
            f'<div class="user-msg">{message}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="bot-msg">{message}</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- INPUT ---------------- #

user_input = st.text_input(
    "Ask anything about AWS, Linux, Git, CI/CD, Kubernetes..."
)

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    response = controller_agent(user_input)
    st.session_state.chat_history.append(("bot", response))
    st.rerun()
