import streamlit as st

with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

st.header('MTA Base')
with open('streamlit_app/home_wrt/text.txt', 'r') as file:
    st.markdown(file.read())
