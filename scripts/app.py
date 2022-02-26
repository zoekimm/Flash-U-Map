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

with open('apikey.txt') as f:
    api_key = f.readline()
    f.close()

def main():

    st.title('Safe-U-Map')
    pages = ['Home', 'Chart', 'Map']
    choice = st.sidebar.radio('Select Pages', pages)
    
    if choice == 'Home':
        #st.subheader('What is Safe-U-Map?')
        col1, col2, col3 = st.columns(3)

        col1.metric('Number of Cases', "70 °F", "1.2 °F")
        col2.metric('Crime Rate', "7", "-8%")
        col3.metric('ss', "86%", "4%")

    elif choice == 'Chart':
        pass
        #show_chart()
    
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
                logit = geodata['results'][0]['geometry']['location']['lng']
        
                m = folium.Map(location= [lat, logit], zoom_start = 16)
                folium_static(m)

                gmaps = googlemaps.Client(key = api_key)

                geocode_result = gmaps.geocode(start)
                print(str(geodata['results'][0]['geometry']['location']['lat'])[0:8])
                print(str(geodata['results'][0]['geometry']['location']['lng'])[0:8])

                user_data = pd.DataFrame()
                
                m = train()
                print(m.predict(pd.DataFrame({'hour': t.hour, 'log' : logit, 'lat' : lat}, index=[0])))

if __name__ == '__main__':
    main()