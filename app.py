from dotenv import load_dotenv

load_dotenv() # load env variable

import streamlit as st 
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# load gemini pro model and get response
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## initialize streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLm Application")

input = st.text_input('input:' ,key='input')
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The Response")
    st.write(response)