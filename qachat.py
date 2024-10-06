from dotenv import load_dotenv

load_dotenv() # load env variable

import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# load gemini pro model and get response
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[]) # Store history

 
def get_gemini_response(question):
    response = chat.send_message(question,stream=True)
    return response

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# initialize session state for chat history

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("input:",key="input")

submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    ## Addding user query to session
    st.session_state['chat_history'].append(("you",input))
    st.subheader("The Response")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("bot",chunk.text))
st.subheader("The chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")

