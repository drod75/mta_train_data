import folium
import pandas as pd
from mta_data_analysis import read_data
from ast import literal_eval

def string_stuff(x):
    x = x.replace('[','').replace(']','').replace(',',' ').replace('\'',' ')
    lst = x.split(' ')
    lst = [a for a in lst if a] 
    return lst
def create_map()  -> folium.Map :
    return folium.Map(location=[40.693943, -73.8], default_zoom_start=55)

def set_markers(map: folium.Map) -> folium.Map :
    locations = pd.read_csv('streamlit_app\data\mta_cleaned_data.csv')
    locations['STATION_LINES'] = locations['STATION_LINES'].apply(string_stuff)
    color_palette = {
        'A':'blue',
        'C':'blue',
        'E':'blue',
        'B':'orange',
        'D':'orange',
        'F':'orange',
        'M':'orange',
        'G':'green',
        'J':'gray',
        'Z':'gray',
        'L':'gray',
        'S':'gray',
        'N':'lightred',
        'Q':'lightred',
        'R':'lightred',
        '1':'red',
        '2':'red',
        '3':'red',
        '6':'darkgreen',
        '5':'darkgreen',
        '4':'darkgreen',
        '7':'purple'
    }
    for index, row in locations.iterrows():
        lst = row['STATION_LINES'][0]
        cl = color_palette[lst]
        folium.Circle(
            location=[row['LATITUDE'],row['LONGITUDE']], 
            radius=row['SUM_RIDERSHIP'],
            color=cl).add_to(map)
    return map

def send_data() -> folium.Map :
    map = create_map()
    map = set_markers(map)
    return map
