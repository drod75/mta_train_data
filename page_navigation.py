import streamlit as st
from mta_data_analysis import read_data

with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)
    st.sidebar.markdown(f'<style>{css.read()}</style>' , unsafe_allow_html=True)


pages = [
    st.Page('app/src/home.py',title='MTA Base', icon=':material/domain:', default=True),
    st.Page('app/src/mta_analysis.py',title='MTA Ridership', icon=':material/groups:'),
    st.Page('app/src/mta_suggestions.py',title='MTA Line Suggestion', icon=':material/subway:'),
    st.Page('app/src/mta_ai.py',title='MT-AI', icon=':material/robot_2:'),
    st.Page('app/src/my.py',title='CREDITS', icon=':material/contact_page:')
]
pg = st.navigation(pages)
read_data()
pg.run()