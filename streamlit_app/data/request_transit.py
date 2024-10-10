import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
import pprint
from google.transit import gtfs_realtime_pb2
import geopandas as gpd

def column_setting(x):
    x = str(x)
    res = x[:4] + '/' + x[4:6] + '/' + x[6:len(x)]
    return res

def request_train_data() -> pd.DataFrame:
    # Define the API endpoint
    urls = ['https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace', 
            'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm',
            'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g', 
            'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz',
            'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw',
            'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l',
            'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs']
    df = pd.DataFrame(
            columns=['trip_id', 'trip_start_time', 'trip_start_date', 'trip_route_id'])
    for url in urls:
        # Obtaining the gtfs feed data
        feed = gtfs_realtime_pb2.FeedMessage()
        response = requests.get(url, allow_redirects=True)
        feed.ParseFromString(response.content)

        # initializing a dataframe
        

        # Parsing the data
        for entity in feed.entity:
            trip_dct = {}
            if entity.HasField('trip_update'):
                trip_update = entity.trip_update
                trip = trip_update.trip

                # appending trip data to dictionary
                trip_dct['trip_id'] = trip.trip_id
                trip_dct['trip_start_time'] = trip.start_time
                trip_dct['trip_start_date'] = trip.start_date
                trip_dct['trip_route_id'] = trip.route_id

            # appending trip dictionary to dataframe
            df = df._append(trip_dct, ignore_index=True)
    df = df.dropna().reset_index()
    df['trip_start_date'] = df['trip_start_date'].apply(column_setting)
    df['trip_route_id'] = df['trip_route_id'].apply(str)
    df['trip_route_id'] = df['trip_route_id'].apply(str.upper)
    df = df[(df['trip_route_id'] != 'FS') & (df['trip_route_id'] != 'GS')]

    return df
