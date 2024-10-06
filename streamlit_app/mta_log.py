import streamlit as st
from streamlit_app.data.request_transit import request_train_data
import pandas

with open("app/styles/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.header('MTA Train Log')

# Displaying train log data
df = request_train_data()
df = df.drop('index', axis=1)
option = st.selectbox(
    'What route would you like to select?',
    ('N','Q','R'),
    index=None,
    placeholder='Waiting...'
)
if option != None:
    st.table(df[df['trip_route_id'] == option])