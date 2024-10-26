import streamlit as st
import requests

with open("app/styles/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True) 

st.header('MTA Log')
st.markdown('### This is the MTA Log page!')