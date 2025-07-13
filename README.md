# 🧠 MindScope: AI Research Insight Generator

**MindScope** is a privacy-focused, AI-powered research assistant built using Streamlit and modern NLP models. It allows users to upload research documents (PDF or TXT), get concise summaries, visualize concept relationships through mind maps, ask intelligent questions, and test their comprehension — all processed locally without storing any data.

---

## 🚀 Features

- 📤 Upload and read PDF/TXT documents
- ✍️ Generate 80–150 word executive summaries
- 🧠 Visualize concept relationships using interactive Mind Maps
- ❓ Ask natural language questions about the content
- 🧪 Test your understanding with AI-generated comprehension questions
- ✅ Receive evaluation feedback on your answers (not based on word-to-word match)
- 🧾 View complete conversation history
- 🧑‍🎨 Modern dark UI with glassmorphism style
- 🔒 No data is stored or shared — runs fully local for privacy

---

## 🖼️ UI Preview

> *(Add a screenshot named `preview-screenshot.png` in your repo)*  
> Example preview showing summary + mind map + Q&A interface.

---

## 🧑‍💻 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io)
- **Models Used**: `roberta-base-squad2` (Hugging Face Transformers)
- **Summarization**: TextRank + Transformer-based methods
- **Visualization**: TF-IDF + TruncatedSVD + Graphviz
- **Answer Evaluation**: Semantic similarity scoring via QA pipeline
- **Styling**: Custom CSS (dark mode, animations, and layout)

---

---

## 🎥 Demo Video

Watch a quick walkthrough of **MindScope** in action:

👉 [Click here to watch the demo on YouTube](https://www.youtube.com/watch?v=your-demo-link)  
[![Watch the video](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

> 📌 *The video shows how to upload a research paper, generate a mind map, ask questions, and test your comprehension interactively.*


---

## ⚙️ Setup Instructions

To run this project locally:

```bash
# Clone the repository
git clone https://github.com/jhagauravkr/MindScope.git
cd MindScope

# Set up virtual environment (recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py


