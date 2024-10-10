import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plots_for_st(df: pd.DataFrame):
    return sns.barplot(x=df['STATION_LINES'], y=df['SUM_RIDERSHIP'], hue=df['BOROUGH'])
