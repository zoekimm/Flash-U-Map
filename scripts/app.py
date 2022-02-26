import streamlit as st
from streamlit_folium import folium_static
import folium
import json
import requests
import googlemaps
import pandas as pd
import numpy as np
import datetime

with open('apikey.txt') as f:
    api_key = f.readline()
    f.close

def main():

    st.title('Safe-U-Map')
    pages = ['Home', 'Chart', 'Map']
    choice = st.sidebar.radio('Select Pages', pages)
    
    if choice == 'Home':
        st.subheader('What is Safe-U-Map?')

    elif choice == 'Chart':
        pass
    
    elif choice == 'Map':
        st.markdown('Map')
        default_value = 'N/A'
        start = st.text_input("Where are you?", default_value)
        destination = st.text_input("Your Destination", default_value)
        t = st.time_input('When?', datetime.time(8, 45))
        if start is not None:

            GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ start +'&key='+ api_key
            geo_response = requests.request("GET", GEOCODE_URL)
            geodata = json.loads(geo_response.text)

            if geodata['status'] != 'ZERO_RESULTS':
                lat = geodata['results'][0]['geometry']['location']['lat']
                long = geodata['results'][0]['geometry']['location']['lng']
        
                m = folium.Map(location= [lat, long], zoom_start = 16)
                folium_static(m)

                gmaps = googlemaps.Client(key = api_key)

                geocode_result = gmaps.geocode(start)
                print(geodata['results'][0]['geometry']['location']['lat'])

                def get_user_data():
                    record_data = {
                        'hour' : t.hour,
                        'lat' : lat,
                        'log' : log
                    }
                    return pd.DataFrame(record_data, index=[0])


if __name__ == '__main__':
    main()