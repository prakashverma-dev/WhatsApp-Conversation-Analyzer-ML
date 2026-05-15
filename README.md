# WhatsApp-Conversation-Analyzer-ML 📊
This project aims to develop a full-stack web application that automates the mining and  visualization of WhatsApp conversation data using Natural Language Processing (NLP) and  Machine Learning techniques.

---

## 🚀 Live Demo

**Deployed Application:** [🔗 https://ml-whatsapp-analyzer.streamlit.app/](https://ml-whatsapp-analyzer.streamlit.app/)



---

## 🚀 Project Overview

**WhatsApp Conversation Data Mining and Visualization System** is a powerful, user-friendly tool that transforms raw WhatsApp chat exports (`.txt` files) into meaningful insights. It uses **Natural Language Processing (NLP)** and **Machine Learning** techniques to analyze conversations and present them through an interactive dashboard.

This project was developed as part of my **M.Tech Thesis** in Artificial Intelligence and Data Science Engineering at **IIT Patna**.

---

## ✨ Key Features

- **Robust Chat Parsing** – Handles multi-line messages, different timestamp formats, and system messages
- **Advanced Sentiment Analysis** – Ensemble model using **VADER + TextBlob**
- **Emotion & Topic Modeling** – LDA-based topic discovery
- **Rich Visualizations** – Interactive charts, heatmaps, word clouds, emoji analysis
- **User-wise & Overall Analysis** – Works for both individual and group chats
- **Modern UI** – Built with **Streamlit** for excellent user experience
- **Privacy Focused** – All processing happens locally on your machine

---

## 🛠️ Tech Stack

- **Backend**: Python 3.11
- **Data Processing**: Pandas, NumPy
- **NLP & ML**: VADER, TextBlob, Gensim (LDA), NLTK
- **Visualization**: Plotly, Matplotlib, Seaborn, WordCloud
- **Frontend**: Streamlit
- **Others**: Emoji, Regex

---

## 📥 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/prakashverma-dev/WhatsApp-Conversation-Analyzer-ML
   cd WhatsApp-Conversation-Analyzer-ML

2. Install dependencies:
    ```bash
    pip install -r requirements.txt

3. Download NLTK stopwords (run once):
    ```bash
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')

4. Run the application locally : 
    ```bash
    streamlit run app.py

## 📋 How to Use

1. Open WhatsApp on your phone
2. Go to the chat you want to analyze → More → Export Chat → Without Media
3. Upload the .txt file in the web app
4. Select user (or Overall) and click "Show Analysis"
5. Explore insights across multiple tabs


## 📊 Features Showcase

- Statistics Dashboard – Total messages, words, media, links
- Timeline Analysis – Monthly & Daily trends
- Activity Heatmap – Most active days and hours
- Sentiment Analysis – Positive, Negative, Neutral with trends
- Word Cloud – Most used words
- Emoji Analysis – Most frequently used emojis
- Most Active Users – In group chats



## 📁 Project Structure

    

    textwhatsapp-chat-analyzer/
    ├── app.py                 # Main Streamlit Application
    ├── preprocessor.py        # Chat preprocessing logic
    ├── helper.py              # All analysis functions
    ├── requirements.txt
    ├── README.md
    ├── screenshots/           # Screenshots of dashboard
    └── notebooks/             # Jupyter notebooks


## 🎯 Future Enhancements

- Media analysis (images & videos using OCR + Vision Models)
- Integration with Large Language Models (LLM) for chat summarization & Q&A
- Real-time chat analysis
- Mobile Application
- Cloud deployment with user authentication


## 📄 Thesis & Documentation
This project is part of my M.Tech Thesis at Indian Institute of Technology Patna under the guidance of Prof. Rajiv Misra.

Full thesis document and detailed report available in the docs/ folder.

# 🙏 Acknowledgments

- **Prof. Rajiv Misra** – Supervisor & HOD, CSE, IIT Patna
- Open-source community (especially WhatsApp chat analyzer GitHub projects)
- Streamlit, Plotly, and VADER teams


# 📧 Contact
**Prakash Kumar Verma**

__M.Tech (Artificial Intelligence and Data Science Engineering)__

**Indian Institute of Technology, Patna**

Feel free to open an issue or contribute!

Star ⭐ this repository if you found it helpful!


