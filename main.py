import streamlit as st
from langchain_helper import get_qa_chain

st.title("Gemini QA ✨")

question = st.text_input("Query: ")
if question:
    chain = get_qa_chain()
    response = chain(question)
    
    st.header("Answer: ")
    st.write(response['result'])
