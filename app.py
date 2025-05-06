import streamlit as st
import requests

# Load resume or profile context
with open("resume_context.txt", "r") as f:
    resume_context = f.read()

# Streamlit UI
st.set_page_config(page_title="Job Chatbot", page_icon="🤖")
st.title("🤖 Ask Me About My Job Profile")
st.write("Type a question about my experience, skills, or resume.")

# User input
user_input = st.text_input(
    "Your Question", placeholder="e.g. What are your main skills?"
)

# Button to send question
if st.button("Ask"):
    if user_input:
        # Prepare prompt
        prompt = f"""
You are a helpful assistant helping answer questions about a job applicant.
Here is their resume:

{resume_context}

Now answer the following question: {user_input}
"""

        # Send request to Ollama (Mistral)
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False},
        )

        if response.status_code == 200:
            answer = response.json()["response"]
            st.success(answer.strip())
        else:
            st.error("Error connecting to Ollama. Is it running?")
