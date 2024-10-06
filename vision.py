from dotenv import load_dotenv

load_dotenv() # load env variable

import streamlit as st 
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# load gemini pro model and get response
model = genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
         response = model.generate_content([image])

    return response.text

## initialize streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini LLm Application")

input = st.text_input('input:' ,key='input')


upload_file = st.file_uploader("choose an Image...",type=['jpg','jpeg','png'])
image = ""

if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image,caption="uploaded Image.",use_column_width=True)


submit = st.button("Tell me about image")
if submit:
    response = get_gemini_response(input,image)
    st.subheader("The Response")
    st.write(response)