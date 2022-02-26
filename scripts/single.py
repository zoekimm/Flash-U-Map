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


df = pd.read_csv('/Users/zoekim/Desktop/g/Flash-U-Map/dataset/dc_crime_add_vars.csv')
with open('apikey.txt') as f:
    api_key = f.readline()
    f.close()

def display_map(start, t):
    GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ start +'&key='+ api_key
    geo_response = requests.request("GET", GEOCODE_URL)
    geodata = json.loads(geo_response.text)

    if geodata['status'] != 'ZERO_RESULTS':
        lat = geodata['results'][0]['geometry']['location']['lat']
        logit = geodata['results'][0]['geometry']['location']['lng']

        #m = folium.Map(location= [lat, logit], zoom_start = 16)
        dc_map = folium.Map(location = [lat, logit], control_scale = True, zoom_start = 15)
        df['count'] = 1
        df_violent = df[df['crimetype'] == 'Violent']
        HeatMap(
                data = df_violent[['YBLOCK', 'XBLOCK', 'count']].groupby(
                    ['YBLOCK', 'XBLOCK']).sum().reset_index().values.tolist(),
                radius = 8,
                max_zoom = 13).add_to(dc_map)
        folium.Marker(
            location=[lat, logit],
            popup = start,
        ).add_to(dc_map)

        folium_static(dc_map)
        #folium_static(m)

        #gmaps = googlemaps.Client(key = api_key)

        #geocode_result = gmaps.geocode(start)
        #print(str(geodata['results'][0]['geometry']['location']['lat'])[0:8])
        #print(str(geodata['results'][0]['geometry']['location']['lng'])[0:8])

        m = train()
        #print(m.predict(pd.DataFrame({'hour': t.hour, 'log' : logit, 'lat' : lat}, index=[0])))
        result = m.predict(pd.DataFrame({'hour': t.hour, 'log' : logit, 'lat' : lat}, index=[0]))

        if result[0] == 1:
            st.error('💡 Be aware. It showed that the location you are heading to could be dangerous at a given time.')
        else:
            st.success('💡 The location you are heading to is safe at the time.')