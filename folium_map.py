import folium
import geopandas as gpd
import pandas as pd

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
    'W': 'lightred',
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

def seperate_locations(x):
    x = (str(x)).replace('-', " ")
    locations = (str(x)).split(' ')
    return ' '.join(locations)

def getcolor(feature):
    if '-' in feature['properties']['name']:
        lst = (feature['properties']['name']).split('-')
        return color_palette[lst[0]]
    return color_palette[str(feature['properties']['name'])]

def create_map() -> folium.Map:
    return folium.Map(location=[40.693943, -73.8], tiles="Cartodb Positron", default_zoom_start=100)


def set_markers(map: folium.Map) -> folium.Map:
    locations = pd.read_csv('app\streamlit_app\data\mta_cleaned_data.csv')
    for index, row in locations.iterrows():
        lst = row['STATION_LINES'].split(' ')
        cl = color_palette[lst[0]]
        calculation = (row['SUM_RIDERSHIP'] /
                       (locations['SUM_RIDERSHIP'].max()))*10
        folium.Circle(
            location=[row['LATITUDE'], row['LONGITUDE']],
            radius=calculation,
            color=cl,
            popup=folium.Popup(row['STATION'], max_width='300%', lazy=True)).add_to(map)
    return map


def set_lines(map: folium.Map) -> folium.Map:
    gdf = gpd.read_file('app\streamlit_app\data\Subway Lines.geojson')
    folium.GeoJson(
        gdf,
        name="MTA Subway Lines",
        style_function=lambda feature: {
            'color': getcolor(feature),  # Customize the line color
            'weight': 3,
            'opacity': 0.6,
        }
    ).add_to(map)

    # Add layer control for switching between layers
    folium.LayerControl().add_to(map)
    return map
    

def send_data() -> folium.Map:
    map = create_map()
    set_markers(map)
    set_lines(map)
    return map