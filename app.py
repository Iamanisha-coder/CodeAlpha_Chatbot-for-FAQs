import streamlit as st
import json
import time
from difflib import get_close_matches

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD CSS ---------------- #

with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# ---------------- LOAD FAQ ---------------- #

with open("faq.json", "r") as f:
    faq = json.load(f)

# ---------------- SESSION STATE ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I'm your AI FAQ Assistant. Ask me anything about Python, AI, Programming or Streamlit."
        }
    ]

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🤖 AI FAQ Assistant")

st.sidebar.markdown("### Quick Questions")

for q in list(faq.keys())[:8]:
    if st.sidebar.button(q):
        st.session_state.messages.append(
            {"role": "user", "content": q}
        )

        st.session_state.messages.append(
            {"role": "assistant", "content": faq[q]}
        )

st.sidebar.markdown("---")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I'm your AI FAQ Assistant."
        }
    ]
    st.rerun()

# ---------------- HEADER ---------------- #

st.markdown(
"""
<div class="hero">

<h1>🤖 AI FAQ Assistant</h1>

<p>Ask anything about Python, AI, Machine Learning and Programming.</p>

</div>
""",
unsafe_allow_html=True
)

# ---------------- DISPLAY CHAT ---------------- #

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ---------------- CHAT INPUT ---------------- #

prompt = st.chat_input("Type your question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

   with st.chat_message("assistant", avatar="🤖"):

    typing = st.empty()

    typing.markdown(
        """
        <div class="typing">
            <span></span>
            <span></span>
            <span></span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    time.sleep(1.5)

    match = get_close_matches(
        prompt,
        faq.keys(),
        n=1,
        cutoff=0.4
    )

    if match:
        answer = faq[match[0]]
    else:
        answer = (
            "😔 Sorry, I couldn't find an answer.<br><br>"
            "💡 Try asking about Python, AI, Machine Learning, Streamlit, or Programming."
        )

    typing.empty()

    st.markdown(answer, unsafe_allow_html=True)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
