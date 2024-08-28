from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os

import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])
def get_gemini_respone(question):
    response = chat.send_message(question,stream=True)
    return response

if 'chat-history' not in st.session_state:
    st.session_state['chat-history']=[]

st.set_page_config(page_title="QnA Demo")
st.header("Gemini LLM Application")
input = st.text_input("Input:", key="input")

submit = st.button("Ask the Question...")

if submit and input:
    response = get_gemini_respone(input)
    st.session_state['chat-history'].append(("You",input))
    for chunk in response:
        st.session_state['chat-history'].append(("Bot",chunk.text))
st.subheader("chat history:")

for role,text in st.session_state['chat-history']:
    st.write(f"{role}:{text}")