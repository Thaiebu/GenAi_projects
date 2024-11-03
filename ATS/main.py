
import google.generativeai as genai
from dotenv import load_dotenv
import fitz  # PyMuPDF4

load_dotenv()
import os
import base64
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
  """
  Gets text from the PDF and generates response using Gemini Flash.

  Args:
      input: User input for the prompt.
      pdf_content: Bytes content of the uploaded PDF.
      prompt: Prompt for Gemini Flash.

  Returns:
      Text response generated by Gemini Flash.
  """
  model = genai.GenerativeModel('gemini-1.5-flash')

  # Extract text from PDF using a library like PyMuPDF
  with fitz.open(stream=pdf_content, filetype="pdf") as doc:
    text = ""
    for page in doc:
      text += page.get_text("text")  # Combine text from all pages

  # Combine user input, extracted text, and prompt
  full_prompt = "\n".join([input, text, prompt])
  response = model.generate_content([full_prompt])
  return response.text


def input_pdf_setup(uploaded_file):
  """
  Opens the uploaded PDF and returns its content as bytes.

  Args:
      uploaded_file: Uploaded PDF file object.

  Returns:
      Bytes content of the uploaded PDF.

  Raises:
      FileNotFoundError: If no file is uploaded.
  """
  if uploaded_file is None:
    raise FileNotFoundError("No file uploaded")
  return uploaded_file.read()


## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


submit1 = st.button("Tell Me About the Resume")

#submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")



   




