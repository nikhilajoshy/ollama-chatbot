# Job Application Chatbot with Mistral + Streamlit

This project creates a local, privacy-friendly chatbot that can answer questions about your job experience and resume — powered by the open-source Mistral-7B model via Ollama and a web interface using Streamlit.

---

## Features

- 🤖 Chatbot interface for answering questions about your experience
- 🧠 Uses Mistral-7B (open-source LLM)
- 🗂️ Loads your resume content from `resume_context.txt`
- 🌐 Simple UI with Streamlit
- 🔐 Runs 100% locally

---

## Requirements

- Python 3.12
- [Ollama](https://ollama.com/download)
- pip packages:
  - `streamlit`
  - `requests`

---

## 🔧 Installation

1. **Install Ollama**

   Download and install Ollama from:  
   👉 https://ollama.com/download

2. **Pull Mistral Model**

   Open your terminal and run:
   ```bash
   ollama run mistral
