import streamlit as st
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

# model loading
load_dotenv(Path(".env"))
model = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        api_key=os.environ.get('GEMINI_API_KEY')
)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", '''You are a helpful assistant that talks about the Metropolitan Transit System, 
                    an NYC based transit system, you give context about the system and even talk 
                    about how it works and its functions'''),
    ("human", "{input}"),
])

chain = prompt_template | model

def generate_response(input_text):
    response = chain.invoke(input_text)
    return response.content

with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

st.header('MT-AI')
st.markdown('### This is the MT-AI page!')

with st.container():
    # Initialize chat 
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is up?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = generate_response(prompt)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})