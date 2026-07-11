# 🤖 AI FAQ Chatbot

An intelligent FAQ Chatbot developed using **Python**, **Streamlit**, **Natural Language Processing (NLP)**, and **Machine Learning**. The chatbot answers user questions by finding the most relevant FAQ using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 📌 Project Description

The AI FAQ Chatbot allows users to ask questions in natural language and receive relevant answers from a predefined FAQ dataset. It uses NLP techniques to preprocess user input and matches it with stored questions to provide accurate responses.

This project was developed as **Task 2** for the **CodeAlpha Artificial Intelligence Internship**.

---

## ✨ Features

- 🤖 AI-powered FAQ chatbot
- 💬 Interactive chat interface
- 🎨 Animated gradient background
- 💎 Glassmorphism UI
- 🧠 NLP preprocessing using NLTK
- 📊 TF-IDF Vectorization
- 🔍 Cosine Similarity matching
- 📜 Chat history
- 🗑️ Clear chat option
- 📱 Responsive and modern design

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NLTK
- Scikit-learn
- NumPy
- Pandas
- JSON
- HTML & CSS

---

## 📂 Project Structure

```
FAQ_Chatbot/
│── app.py
│── faq.json
│── requirements.txt
│── README.md
│
├── style.css
│   
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <https://github.com/Iamanisha-coder/CodeAlpha_Chatbot-for-FAQs>
```

### 2. Open the project folder

```bash
cd app.py
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. Loads the FAQ dataset from `faq.json`.
2. Preprocesses text using NLTK.
3. Converts FAQ questions into TF-IDF vectors.
4. Accepts a user's question.
5. Calculates Cosine Similarity.
6. Returns the most relevant answer.

---

## 🚀 Future Improvements

- Voice input and speech output
- OpenAI API integration
- Multi-language support
- Database connectivity
- User authentication
- Dark/Light mode
- Context-aware conversations

---

## 👩‍💻 Developed By

**Anisha Tripathi**

CodeAlpha AI Internship – Task 2

---

## 📄 License

This project is created for educational and internship purposes.
