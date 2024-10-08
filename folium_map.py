import folium
import pandas as pd
from mta_data_analysis import read_data
from ast import literal_eval

# loading dataframe for two methods, to prevent it loading multiple times for no reason

# loading the color palette
color_palette = {
    'A': 'blue',
    'C': 'blue',
    'E': 'blue',
    'B': 'orange',
    'D': 'orange',
    'F': 'orange',
    'M': 'orange',
    'G': 'green',
    'J': 'gray',
    'Z': 'gray',
    'L': 'gray',
    'S': 'gray',
    'N': 'lightred',
    'Q': 'lightred',
    'R': 'lightred',
    '1': 'red',
    '2': 'red',
    '3': 'red',
    '6': 'darkgreen',
    '5': 'darkgreen',
    '4': 'darkgreen',
    '7': 'purple'
}


def create_map() -> folium.Map:
    read_data()
    return folium.Map(location=[40.693943, -73.8], default_zoom_start=100)


def set_markers(map: folium.Map) -> folium.Map:
    locations = pd.read_csv('streamlit_app\data\mta_cleaned_data.csv')
    for index, row in locations.iterrows():
        lst = row['STATION_LINES'].split(' ')
        cl = color_palette[lst[0]]
        calculation = (row['SUM_RIDERSHIP'] /
                       (locations['SUM_RIDERSHIP'].max()))*10
        folium.Circle(
            location=[row['LATITUDE'], row['LONGITUDE']],
            radius=calculation,
            color=cl,
            popup=row['STATION']).add_to(map)
    return map


def set_lines(map: folium.Map) -> folium.Map:
    locations = pd.read_csv('streamlit_app\data\mta_cleaned_data.csv')
    lines = [
        'A','C', 'E', 'B', 'D', 'F', 'M', 'G',
        'J', 'Z', 'L', 'S', 'N', 'Q', 'R',
        '1', '2', '3', '6', '5', '4', '7'
             ]
    for l in lines:
        localls = []
        for index, row in locations.iterrows():
            if l in row['STATION_LINES']:
                localls.append([row['LATITUDE'], row['LONGITUDE']])
            else:
                pass
        cl = color_palette[l]
        folium.PolyLine(locations=localls, popup=l, color=cl, weight=2).add_to(map)
    return map
    

def send_data() -> folium.Map:
    map = create_map()
    map = set_markers(map)
    map = set_lines(map)
    return map
