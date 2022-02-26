import streamlit as st
from streamlit_folium import folium_static
import folium
import json
import requests

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


        GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ start +'&key='+ api_key
        geo_response = requests.request("GET", GEOCODE_URL)
        geodata = json.loads(geo_response.text)
        print(geodata)
        
        m = folium.Map(location=[39.949610, -75.150282], zoom_start = 16)
        folium_static(m)

if __name__ == '__main__':
    main()