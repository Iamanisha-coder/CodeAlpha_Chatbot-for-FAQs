import streamlit as st
import json
import os
import time
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------- Download NLTK --------------------
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- Load CSS --------------------
css_file = os.path.join("css", "style.css")

if os.path.exists(css_file):
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------- Animated Background --------------------
st.markdown("""
<div class="glow"></div>
<div class="glow2"></div>
""", unsafe_allow_html=True)

# -------------------- Sidebar --------------------
with st.sidebar:

    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=120)

    st.title("🤖 AI FAQ Chatbot")

    st.markdown("---")

    st.write("### 💡 Suggested Questions")

    suggestions = [
        "What is AI?",
        "What is Machine Learning?",
        "What is Python?",
        "What is NLP?",
        "What is Deep Learning?"
    ]

    for q in suggestions:
        st.write("•", q)

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------------------- Title --------------------
st.markdown("""
<h1 class='title'>
🤖 AI FAQ Assistant
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p class='subtitle'>
Ask me anything about Artificial Intelligence, Python,
Machine Learning and NLP.
</p>
""", unsafe_allow_html=True)

# -------------------- Load FAQ --------------------
with open("faq.json", "r", encoding="utf-8") as file:
    faq = json.load(file)

questions = [item["question"] for item in faq]
answers = [item["answer"] for item in faq]

# -------------------- NLP --------------------
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess(text):

    text = text.lower()

    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    words = nltk.word_tokenize(text)

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

processed_questions = [
    preprocess(q)
    for q in questions
]

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(
    processed_questions
)

# -------------------- Session State --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- Welcome Message --------------------
if len(st.session_state.messages) == 0:

    st.session_state.messages.append({
        "role":"assistant",
        "content":"👋 Hello! I'm your AI FAQ Assistant. Ask me anything!"
    })
    # -------------------- Display Chat History --------------------
for message in st.session_state.messages:

    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])

    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"])


# -------------------- Chat Input --------------------
user_input = st.chat_input("💬 Type your question here...")

if user_input:

    # Show User Message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Typing Animation
    with st.chat_message("assistant"):

        typing = st.empty()

        typing.markdown("""
        <div class="typing">
            <span></span>
            <span></span>
            <span></span>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(1.5)

        # -------------------- AI Logic --------------------
        processed_input = preprocess(user_input)

        input_vector = vectorizer.transform([processed_input])

        similarity = cosine_similarity(
            input_vector,
            question_vectors
        )

        best_index = similarity.argmax()

        confidence = similarity[0][best_index]

        if confidence >= 0.35:

            answer = answers[best_index]

        else:

            answer = (
                "😔 Sorry, I couldn't find an answer to that question.\n\n"
                "Try asking about:\n"
                "- Artificial Intelligence\n"
                "- Machine Learning\n"
                "- Python\n"
                "- Deep Learning\n"
                "- NLP"
            )

        typing.empty()

        st.markdown(answer)

    # Save Bot Response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


# -------------------- Footer --------------------
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<hr style="border:1px solid rgba(255,255,255,0.2);">

<div style="text-align:center; color:white;">

<h4>🤖 AI FAQ Chatbot</h4>

<p>
Built using
<b>Python</b> •
<b>Streamlit</b> •
<b>NLTK</b> •
<b>Scikit-Learn</b>
</p>

<p style="color:#bdbdbd;">
Made with ❤️ by <b>Anisha Tripathi</b>
</p>

</div>
""", unsafe_allow_html=True)
