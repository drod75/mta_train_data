import streamlit as st

with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)
    st.sidebar.markdown(f'<style>{css.read()}</style>' , unsafe_allow_html=True)

st.header('MT-AI')