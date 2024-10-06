import streamlit as st
import folium
from streamlit_folium import st_folium
import extra_streamlit_components as stx
import pandas as pd
from mta_data_analysis import read_data


with open("app/styles/style.css") as css:
    st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

st.header('MTA Riderships')
read_data()
# Set Tabs
chosen_id = stx.tab_bar(data=[
    stx.TabBarItemData(id=1, title="Map",
                       description="A map of MTA Subway Stations"),
    stx.TabBarItemData(id=2, title="Analysis",
                       description="An analysis of MTA Ridership"),
    stx.TabBarItemData(id=3, title="Train Line Creation",
                       description="An analysis of possible train lines"),
], default=1)

# Set tab content, for some reason id is set to number but represented a string, took me a while to notice
match chosen_id:
    # Tab one map w Markers(pending)
    case '1':
        m = folium.Map(location=[40.693943, -73.8], default_zoom_start=55)
        st_folium(m, width=1000)
    # Tab two data viewing
    case '2':
        df = pd.read_csv('streamlit_app\data\mta_cleaned_data.csv')
        option = st.selectbox('What Borough would you like to see?', ('Brooklyn', 'Manhattan',
                              'Queens', 'Bronx', 'ALL'), index=None, placeholder='Please Select a choice...')
        # Option 1, borough
        match option:
            case 'ALL':
                option2 = st.selectbox('The table comes with 489 entries, would you like to see data from the bottom or top?', (
                    'Top', 'Bottom'), index=None, placeholder='Please Select a choice...')
                option3 = st.slider('Pick a number', 0, 389)
                # Option 2, top or bottom of all, and how many
                match option2:
                    case 'Top':
                        st.table(df.head(option3))
                    case 'Bottom':
                        st.table(df.tail(option3))
            case 'Brooklyn':
                slc = df[df['BOROUGH'] == 'Brooklyn']
                st.table(slc)
            case 'Manhattan':
                slc = df[df['BOROUGH'] == 'Manhattan']
                st.table(slc)
            case 'Queens':
                slc = df[df['BOROUGH'] == 'Queens']
                st.table(slc)
            case 'Bronx':
                slc = df[df['BOROUGH'] == 'Bronx']
                st.table(slc)
    # Tab three possible train lines
    case '3':
        st.write('No')
