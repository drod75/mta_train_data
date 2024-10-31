import plotly.express as px
import pandas as pd
import streamlit as st
import streamlit_folium as st_folium
import folium
import seaborn as sns
import matplotlib.pyplot as plt
from folium.plugins import HeatMap

def plots_for_st(df: pd.DataFrame):
    option = st.selectbox('What Borough would you like to analyze?', ['Manhattan', 'Bronx', 'Brooklyn', 'Queens', 'ALL'], index=None, placeholder='Select a Borough')
    figure_list = []
    match option:
        case 'ALL':
            ridership = df['SUM_RIDERSHIP']
            m = folium.Map(location=[40.779393,-73.966847], zoom_start=10, tiles="Cartodb Positron")
            HeatMap(list(zip(df['LATITUDE'], df['LONGITUDE'], ridership)), radius=10).add_to(m)
            st_folium.folium_static(m)
            st.pyplot(sns.pairplot(df, hue='BOROUGH'))

        case 'Manhattan':
            df_manhattan = df[df['BOROUGH'] == 'Manhattan']
            ridership = df_manhattan['SUM_RIDERSHIP']
            m = folium.Map(location=[40.779393,-73.966847], zoom_start=12, tiles="Cartodb Positron")
            HeatMap(list(zip(df_manhattan['LATITUDE'], df_manhattan['LONGITUDE'], ridership)), radius=10).add_to(m)
            st_folium.folium_static(m)
            st.pyplot(sns.pairplot(df_manhattan, hue='STATION_LINES'))
        case 'Bronx':
            df_bronx = df[df['BOROUGH'] == 'Bronx']
            ridership = df_bronx['SUM_RIDERSHIP']
            m = folium.Map(location=[40.845881,-73.876357], zoom_start=12, tiles="Cartodb Positron")
            HeatMap(list(zip(df_bronx['LATITUDE'], df_bronx['LONGITUDE'], ridership)), radius=10).add_to(m)
            st_folium.folium_static(m)
            st.pyplot(sns.pairplot(df_bronx))        
        case 'Brooklyn':
            df_brooklyn = df[df['BOROUGH'] == 'Brooklyn']
            ridership = df_brooklyn['SUM_RIDERSHIP']
            m = folium.Map(location=[40.646641,-73.955603], zoom_start=12, tiles="Cartodb Positron")
            HeatMap(list(zip(df_brooklyn['LATITUDE'], df_brooklyn['LONGITUDE'], ridership)), radius=10).add_to(m)
            st_folium.folium_static(m)  
            st.pyplot(sns.pairplot(df_brooklyn))
        case 'Queens':
            df_queens = df[df['BOROUGH'] == 'Queens']
            ridership = df_queens['SUM_RIDERSHIP']
            m = folium.Map(location=[40.711386,-73.827573], zoom_start=12, tiles="Cartodb Positron")
            HeatMap(list(zip(df_queens['LATITUDE'], df_queens['LONGITUDE'], ridership)), radius=10).add_to(m)
            st_folium.folium_static(m)
            st.pyplot(sns.pairplot(df_queens))
    return figure_list
