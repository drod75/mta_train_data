import streamlit as st

with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)

st.header('CREDITS')
st.markdown('### This is the Credits page!')

with open('app/src/writing/credits.txt', 'r') as file:
    st.markdown(file.read())
