import streamlit as st

with open("app/styles/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.header('MTA Line Suggestion')
st.markdown('### This is the MTA Line Suggestion page!')
