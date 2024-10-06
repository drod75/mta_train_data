import streamlit as st

with open( "app/styles/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html=True)
pages = [
    st.Page('streamlit_app/home.py',title='MTA Base', icon=':material/domain:', default=True),
    st.Page('streamlit_app/mta_log.py',title='MTA Train Log', icon=':material/subway:'),
    st.Page('streamlit_app/mta_analysis.py',title='MTA Ridership', icon=':material/groups:'),
    st.Page('streamlit_app/mta_ai.py',title='MT-AI', icon=':material/robot_2:')
]
pg = st.navigation(pages)
pg.run()