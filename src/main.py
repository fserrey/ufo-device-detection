import pandas as pd
import numpy as np
import folium

df = pd.read_csv("ufo.csv", parse_dates=['datetime'])

def search_ufo_device(DataFrame, date, country, range):
    """
    With this function we filter dataframe for the values we are looking for
    :param DataFrame: Given dataframe with all features
    :param date: String format of datetime search starting point ("Year-month-day")
    :param country: Country in which we are looking for.
    :param range: Int radius of effectiveness (km)
    :return: Location or list of locations
    """
    # First we select columns we want and set datetime as index
    df = DataFrame[["datetime","city","country", "distance", "latitude", "longitude"]]
    df["datetime"] = df['datetime'].str.replace('24:00', '0:00')
    df["datetime"] = pd.to_datetime(df["datetime"], format = "%m/%d/%Y %H:%M")
    df.set_index('datetime', inplace=True)

    # Second, we apply filters by params inserted
    ufo_dev = df.loc[date + " " + "00:00":]
    ufo_dev = ufo_dev[ufo_dev['country'].str.contains("us")]
    ufo_dev = ufo_dev[(ufo_dev['distance'] >= 300) & (ufo_dev['distance'] <= 400)]
