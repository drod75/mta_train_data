import pandas as pd
def seperate_locations(x):
    x = (str(x)).replace(')', "")
    locations = (str(x)).split('(')
    lst = locations[-1].split(',')
    return list(lst)

def read_data():
    # reading data
    df = pd.read_json('https://data.ny.gov/resource/wujg-7c2s.json?$query=SELECT%0A%20%20sum(%60ridership%60)%20AS%20%60sum_ridership%60%2C%0A%20%20%60borough%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60longitude%60%2C%0A%20%20%60station_complex_id%60%2C%0A%20%20%60station_complex%60%0AWHERE%0A%20%20%60transit_timestamp%60%0A%20%20%20%20BETWEEN%20%222024-01-01T00%3A00%3A00%22%20%3A%3A%20floating_timestamp%0A%20%20%20%20AND%20%222024-10-01T15%3A50%3A52%22%20%3A%3A%20floating_timestamp%0AGROUP%20BY%0A%20%20%60station_complex_id%60%2C%0A%20%20%60station_complex%60%2C%0A%20%20%60borough%60%2C%0A%20%20%60latitude%60%2C%0A%20%20%60longitude%60')
    
    #adjusting data
    df = df[['station_complex_id','station_complex','borough','latitude','longitude','sum_ridership']]
    df = df.rename(columns={'station_complex_id':'station_id', 'station_complex':'station'})
    df.columns = df.columns.str.upper()
    df['STATION_LINES'] = df['STATION'].apply(seperate_locations)
    
    #done with data :)
    df.to_csv('streamlit_app\data\mta_cleaned_data.csv',index=False)