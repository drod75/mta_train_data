import plotly.express as px
import pandas as pd

def plots_for_st(df: pd.DataFrame):
    fig1 = px.bar(df, x='BOROUGH', y='SUM_RIDERSHIP', color='BOROUGH', title='Ridership by Stations')
    
    fig2 = px.treemap(df[df['BOROUGH'] == 'Manhattan'],values='SUM_RIDERSHIP', names='STATION', parents='BOROUGH',title='Manhattan Treemap')
    fig3 = px.treemap(df[df['BOROUGH'] == 'Bronx'],values='SUM_RIDERSHIP', names='STATION', parents='BOROUGH', title='Bronx Treemap')
    fig4 = px.treemap(df[df['BOROUGH'] == 'Brooklyn'],values='SUM_RIDERSHIP', names='STATION', parents='BOROUGH', title='Brooklyn Treemap') 
    fig5 = px.treemap(df[df['BOROUGH'] == 'Queens'],values='SUM_RIDERSHIP', names='STATION', parents='BOROUGH', title='Queens Treemap')
 
    return [fig1,fig2,fig3,fig4,fig5]