import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # reads your .env file

client = OpenAI(
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)
MODEL = os.getenv("LLM_MODEL")

st.title("My first AI app")

question = st.text_input("Ask anything")

if st.button("Ask") and question:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": question}],
            )
            st.write(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Something went wrong: {e}")