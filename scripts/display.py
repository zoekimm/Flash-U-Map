import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def show_chart():
    df = pd.read_csv('/Users/zoekim/Desktop/g/Safe-U-Map/dc_crime_add_vars.csv')
    fig = plt.figure(figsize = (5, 5))
    plt.style.use('seaborn')
    color = plt.cm.cool(np.linspace(0, 1, 15))
    df['OFFENSE'].value_counts().plot.bar(color = color, figsize = (5, 5))
    plt.title('Crime by Offense Type',fontsize = 20)
    plt.ylabel("Number of Cases", fontsize = 20)
    plt.xticks(rotation = 90)
    st.pyplot(fig)
    return