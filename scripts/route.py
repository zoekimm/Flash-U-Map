import streamlit as st
from streamlit_folium import folium_static
import folium
import json
import requests
import googlemaps
import pandas as pd
import numpy as np
import datetime
from display import show_chart
from build import train
from folium.plugins import HeatMap

with open('apikey.txt') as f:
    api_key = f.readline()
    f.close()


def display_route(start, dest, t):
    gmaps = googlemaps.Client(key = api_key)

    geocode_start = gmaps.geocode(start)
    geocode_dest = gmaps.geocode(dest)

    print(geocode_start['results'])

    def get_coordinates(geodata):
        return str(geodata['results'][0]['geometry']['location']['lat']) + ',' + str(geodata['results'][0]['geometry']['location']['lng'])

    directions_result = gmaps.directions(get_coordinates(geocode_start), get_coordinates(geocode_dest), mode = "driving", departure_time = datetime.datetime.now(), avoid = 'tolls')

    st.markdown('Distance:' + directions_result.get("legs")[0].get("distance"))
    st.markdown('Duration:' + directions_result.get("legs")[0].get("duration"))

