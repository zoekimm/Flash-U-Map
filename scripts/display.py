import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import zipfile
import requests

import zipfile

zf = zipfile.ZipFile('dc_crime_add_vars.csv.zip') 
df = pd.read_csv(zf.open('dc_crime_add_vars.csv'))

def show_chart():

    st.subheader('💡 At a Glance')
    
    option = st.selectbox('Plot Type', ('Count Plot', 'Heatmap'))

    container1 = st.container()
    col1, col2 = st.columns(2)

    if option == 'Count Plot':
        #fig, ax = plt.subplots()
        with container1:
            with col1:
                fig_c = plt.figure()
                plt.title('Frequency of Crime by Time', fontsize = 20)
                ax = sns.countplot(x = 'SHIFT', data = df)
                plt.ylabel("Number of Cases", fontsize = 20)
                plt.xticks(rotation = 0)
                st.pyplot(fig_c)
            with col2:
                fig_o = plt.figure()
                plt.title('Frequency of Crime by Offense Type', fontsize = 20)
                ax = sns.countplot(x = 'OFFENSE', data = df)
                plt.ylabel("Number of Cases", fontsize = 20)
                plt.xticks(rotation = 90)
                st.pyplot(fig_o)
        
        container2 = st.container()
        col3, col4 = st.columns(2)

        #fig, ax = plt.subplots()
        with container2:
            with col3:
                fig_h = plt.figure()
                plt.title('Frequency of Crime by Hour', fontsize = 20)
                ax = sns.countplot(x = 'hour', data = df)
                plt.ylabel("Number of Cases", fontsize = 20)
                plt.xticks(rotation = 0)
                st.pyplot(fig_h)
            with col4:
                fig_m = plt.figure()
                plt.title('Frequency of Crime by Month', fontsize = 20)
                ax = sns.countplot(x = 'month', data = df)
                plt.ylabel("Number of Cases", fontsize = 20)
                plt.xticks(rotation = 90)
                st.pyplot(fig_m)

    elif option == 'Heatmap':
        dc_map = folium.Map(location = [38.9072, -77.0369], control_scale = True, zoom_start = 14)
        df['count'] = 1
        df_violent = df[df['crimetype'] == 'Violent']
        HeatMap(data = df_violent[['YBLOCK', 'XBLOCK', 'count']].groupby(
                ['YBLOCK', 'XBLOCK']).sum().reset_index().values.tolist(),
                radius = 8,max_zoom = 13).add_to(dc_map)
        folium_static(dc_map)


    return