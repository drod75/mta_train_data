import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI


with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

st.header('MT-AI')
st.markdown('### This is the MT-AI page!')

st.title("🦜🔗 Quickstart App")

def generate_response(input_text):
    model = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What is the MTA?",
    )
    submitted = st.form_submit_button("Submit")
    generate_response(text)