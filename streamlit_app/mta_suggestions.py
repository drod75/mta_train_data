import streamlit as st
from streamlit_app.data.request_transit import request_train_data
import pandas

with open("app/styles/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.header('MTA Line Suggestion')
