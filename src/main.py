import pandas as pd
import folium
from functions import search_ufo_device

# Question
# Our data science team has predicted that the Earth is going to be invaded by an alien force in the
# next years. Our only hope is to replicate a device that can block all alien technology in a radius of
# ~300km. Sadly, the device was sold in 2004 to an anonymous buyer to protect her hometown and
# we don't know how contact her again. We know that the device has been active since 2004 in one
# city in the USA, and we want to know where to start our search.


# First, we import dataset and parse time
df = pd.read_csv("ufo.csv", parse_dates=['datetime'])

# Let's remember the conditions:
    # Must be from 2004 onwards
    # Must be in the USA (Oh wait!)
    # The application radious must be around 300 km effective

# We import the function we created ad hoc for this assessment

search_ufo_device(DataFrame = df, date = "2004-01-01", country = "USA", min_range = 300)

