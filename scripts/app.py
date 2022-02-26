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
from single import display_map
from route import display_route

with open('apikey.txt') as f:
    api_key = f.readline()
    f.close()

df = pd.read_csv('/Users/zoekim/Desktop/g/Flash-U-Map/dataset/dc_crime_add_vars.csv')

def main():

    st.set_page_config(
        page_title = 'Flash-U-Map 🔦 ',
        layout="centered",
        initial_sidebar_state="expanded",
    )

    st.title('Flash-U-Map 🔦 ')
    pages = ['Home', 'Chart', 'Locate Me', 'Guide Me']
    choice = st.sidebar.radio('Select Pages', pages)
    
    if choice == 'Home':
        #st.subheader('What is Safe-U-Map?')
        col1, col2, col3 = st.columns(3)
        col1.metric('Violent Crime', "699 Cases", "23%")
        col2.metric('Property Crime', "3272 Cases", "7%")
        col3.metric('All Crime', "3971 Cases", "10%")

        st.subheader('💡 At a Glance')

        dc_map = folium.Map(location = [38.9072, -77.0369], control_scale = True, zoom_start = 14)
        df['count'] = 1
        df_violent = df[df['crimetype'] == 'Violent']
        HeatMap(data = df_violent[['YBLOCK', 'XBLOCK', 'count']].groupby(
                ['YBLOCK', 'XBLOCK']).sum().reset_index().values.tolist(),
                radius = 8,max_zoom = 13).add_to(dc_map)
        folium_static(dc_map)

    elif choice == 'Chart':
        pass
        #show_chart()
    
    elif choice == 'Locate Me':
        st.subheader('💡 Flash your Place')
        default_value = 'Georgetown University'
        start = st.text_input("Where do you want to go?", default_value)
        t = st.time_input('When are you going?', datetime.time(12, 00))

        if start is not None:
            display_map(start, t)

    elif choice == 'Guide Me':
        st.subheader('💡 Flash your Route')
        default_value = 'Georgetown University'
        default_value2 = 'National Mall'
        start = st.text_input("Where do you want to go?", default_value)
        destination = st.text_input("Your Destination", default_value2)
        t = st.time_input('When are you going?', datetime.time(12, 00))

        if start is not None:
            display_route(start, dest, t)

if __name__ == '__main__':
    main()