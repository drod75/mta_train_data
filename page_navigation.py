import streamlit as st
from mta_data_analysis import read_data

with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)
    st.sidebar.markdown(f'<style>{css.read()}</style>' , unsafe_allow_html=True)


pages = [
    st.Page('app/streamlit_app/home.py',title='MTA Base', icon=':material/domain:', default=True),
    st.Page('app/streamlit_app/mta_analysis.py',title='MTA Ridership', icon=':material/groups:'),
    st.Page('app/streamlit_app/mta_suggestions.py',title='MTA Line Suggestion', icon=':material/subway:'),
    st.Page('app/streamlit_app/mta_ai.py',title='MT-AI', icon=':material/robot_2:')
]
pg = st.navigation(pages)
read_data()
pg.run()