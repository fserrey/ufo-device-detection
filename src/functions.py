import pandas as pd
import folium
import webbrowser
import sys
import os
import warnings

if not sys.warnoptions:
    warnings.simplefilter("ignore")

def search_ufo_device(DataFrame, date = "2004-01-01", country = "USA", min_range = 300):
    """
    With this function we filter dataframe for the values we are looking for
    :param DataFrame: Given dataframe with all features
    :param date: String format of datetime search starting point ("Year-month-day")
    :param country: Country in which we are looking for.
    :param range: Integer - radius of minimum effectiveness (km)
    :return: Location or list of locations
    """
    # First we select columns we want and set datetime as index
    df = DataFrame[["datetime","city","country", "distance", "latitude", "longitude"]]
    df.dropna(inplace = True)
    df["datetime"] = df['datetime'].str.replace('24:00', '0:00')
    df["datetime"] = pd.to_datetime(df["datetime"], format = "%m/%d/%Y %H:%M")
    df.set_index('datetime', inplace=True)

    # Second, we apply filters by params inserted
    ufo_dev = df.loc[date + " " + "00:00":] # Datetime filter

    # Country filter
    country_label = {'us':"USA", 'gb':"Great Britain", 'ca': "Canada", 'au':"Australia", 'de':"Germany"}
    for label, name in country_label.items():
        if name == country:
            ufo_dev = ufo_dev[ufo_dev['country'].str.contains(label)]
    # Range filter
    ufo_def = ufo_dev[(ufo_dev['distance'] >= min_range) & (ufo_dev['distance'] <= min_range + 50)]

    print(f"The town we are looking for is:")
    print(ufo_dev.loc[ufo_dev["distance"].idxmin()])

    # Let's print it in a map!
    location = ufo_dev[['latitude', 'longitude']][ufo_dev["distance"].idxmin().strftime('%Y-%m-%d %H:%M:%S')]
    mapa = folium.Map(
        location=location,
        zoom_start=12,
        tiles='Stamen Terrain'
        )
    folium.Marker(location).add_to(mapa)
    mapa.save("ufo_device_location.html")


    filename = 'ufo_device_location.html'
    return webbrowser.open('file://' + os.path.realpath(filename))
