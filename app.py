import streamlit as st
import json
import time
from difflib import get_close_matches

# ---------------- Page Configuration ---------------- #
st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Load CSS ---------------- #
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---------------- Load FAQ ---------------- #
with open("faq.json", "r") as f:
    faq = json.load(f)

# ---------------- Session State ---------------- #
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I'm your AI FAQ Assistant. Ask me anything about Python, AI, Programming, or Streamlit."
        }
    ]

# ---------------- Sidebar ---------------- #
st.sidebar.title("🤖 AI FAQ Assistant")

st.sidebar.markdown("### 📚 Frequently Asked Questions")

for question in faq.keys():
    if st.sidebar.button(question):
        st.session_state.messages.append(
            {"role": "user", "content": question}
        )
        st.session_state.messages.append(
            {"role": "assistant", "content": faq[question]}
        )
        st.rerun()

st.sidebar.markdown("---")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "👋 Hello! I'm your AI FAQ Assistant."
        }
    ]
    st.rerun()

# ---------------- Header ---------------- #
st.markdown(
"""
<div class="hero">
<h1>🤖 AI FAQ Assistant</h1>
<p>Your smart assistant for Programming FAQs</p>
</div>
""",
unsafe_allow_html=True
)

# ---------------- Chat History ---------------- #
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- User Input ---------------- #
prompt = st.chat_input("Ask your question here...")

if prompt:

    # User Message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Reply
    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):
            time.sleep(1)

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
                    "❌ Sorry, I don't know the answer.\n\n"
                    "Try asking another programming-related question."
                )

        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# ---------------- Footer ---------------- #
st.markdown(
"""
<hr>
<center>
Made with ❤️ by <b>Anisha Tripathi</b><br>
CodeAlpha Python Programming Internship
</center>
""",
unsafe_allow_html=True
)
