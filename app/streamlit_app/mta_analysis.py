import streamlit as st
import streamlit_folium as st_folium
import extra_streamlit_components as stx
import pandas as pd
from folium_map import send_data
from plots_st import plots_for_st


with open("app/styles/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.header('MTA Riderships')
st.markdown('### This is the MTA Ridership page!')

# Set Tabs
chosen_id = stx.tab_bar(data=[
    stx.TabBarItemData(id=1, title="Map",
                       description="A map of MTA Subway Stations"),
    stx.TabBarItemData(id=2, title="Ridership Overview",
                       description="An overview of MTA Ridership"),
    stx.TabBarItemData(id=3, title='Ridership Analysis',
                       description='An analysis of MTA Ridership')
], default=1)

df = pd.read_csv('app/streamlit_app/data/mta_cleaned_data.csv')
# Set tab content, for some reason id is set to number but represented a string, took me a while to notice
match chosen_id:
    # Tab one map w Markers
    case '1':
        with st.container(border=True):
            st_folium.folium_static(send_data())
    # Tab two data viewing
    case '2':
        option = st.selectbox('What Borough would you like to see?', ('Brooklyn', 'Manhattan',
                'Queens', 'Bronx', 'ALL'), index=None, placeholder='Please Select a choice...')
        if option =='ALL':
            option2 = st.selectbox('The table comes with 485 entries, would you like to see data from the bottom or top?', (
                    'Top', 'Bottom'), index=None, placeholder='Please Select a choice...')
            option3 = st.slider('Pick a number', 0, 485)
            # Option 2, top or bottom of all, and how many
            while option2 != None:
                match option2:
                    case 'Top':
                        slc = df.head(option3)
                        slc = slc.sort_values('SUM_RIDERSHIP', ascending=False)
                        st.table(slc)
                    case 'Bottom':
                        slc = df.tail(option3)
                        slc = slc.sort_values('SUM_RIDERSHIP', ascending=False)
                        st.table(slc)
        else:
            slc = df[df['BOROUGH'] == option]
            slc = slc.sort_values('SUM_RIDERSHIP', ascending=False)
            st.table(slc)
    # Tab Three plots
    case '3':
        with st.container(border=True):
            figs = plots_for_st(df)
            for fig in figs:
                st.plotly_chart(fig)
