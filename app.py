import os
import streamlit as st
from constants import Google_Api_Key
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

# from langchain.memory import ConversationBufferMemory

os.environ['Google_Api_Key']=Google_Api_Key
genai.configure(api_key=os.environ['Google_Api_Key'])

st.title("Demo LLM with langchain and Gemini Pro")
input_text=st.text_input("Proide your resume in form of text here")

llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=Google_Api_Key)

template="You have a resume {text} that needs to be parsed into a structured JSON format. The resume includes sections like personal information, education, projects, skills, achievements, and profile links.Convert it into JSON format. Assume the resume is provided as a plain text string with sections ending in colons (:) or bold bigger size headings with underline"

template1=PromptTemplate(
    input_variables=['text'],
    template=template
)
chain=LLMChain(llm=llm,prompt=template1,verbose='true')
if input_text:
    st.write(chain.run(input_text))
