"""
Visualisation of the filters
The user have to select the telescopes he want to display. For each selected telescope,
a new section will appear in the left panel, to chose the instrument corresponding to the 
telescope. 

The filters information are stored in the instruments file (/telescopes/instruments.py)
For each selection, the dictionary info from /telescopes/main_info is read.
The structure is as follow. To read Euclid's NIR's Y band, we read:
     - info['Euclid']["Instruments"]['Euclid_NIR']["bands"][Y]

By default, when selecting an instrument, all bands are displayed, but you can then remove some.
For some, you can also restrict to a survey, become some surveys do not use the whole range of the instrument's filters

The plotting is done by plot_bands in /utils/plot.py
"""


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from telescopes.main_info import info
from utils.plots import plot_bands
from telescopes.references import filters_refs


# SurViZ logo
#st.image('surviz_black_long.png')
df= pd.read_csv('/workspaces/SurViZ/data/4- international-tourist-trips.csv')
df1=pd.read_csv('/workspaces/SurViZ/data/10- average-length-of-stay.csv')
df2= pd.read_csv('/workspaces/SurViZ/data/20- average-expenditures-of-tourists-abroad.csv')

# Description and README. The references are in filters_ref in /telescopes/references.py
#st.markdown('# 🌐 Global visualisation \n ')
#description = st.expander("README")
#description.markdown(filters_refs)
#st.markdown('You can see here the filters of the different instruments. Note that for now, shapes and sensitivities of each filter are not correct: the y-axis is arbitrary, and the differences in height are just here for a better visualisation')
#st.markdown('Select on the left panel the missions and instruments you want to display')

# Markdown section to display instructions
st.markdown("## Total Tourists by Year and Country 👨‍👩‍👦‍👦")
#st.markdown("Please select one or more countries from the list below:")
selected_countries = st.multiselect("Select Countries", df['Entity'].unique())
filtered_df = df[df['Entity'].isin(selected_countries)]
#st.write("### Selected Data")
#st.write(filtered_df)
if not filtered_df.empty:
    fig = px.line(filtered_df, x='Year', y='Inbound arrivals (tourists)', color='Entity', title='Total Tourists by Year and Country ',labels={'Entity': 'Country'})
    st.plotly_chart(fig)
else:
    st.write("No data available for the selected countries.")


# Multi Select the telescopes. Default Euclid, Rubin/LSST
#telescopes = st.sidebar.multiselect(
 #       "Select the telescopes",
  #      list(info.keys()),
   #     default=["Euclid", 'Rubin']
    #)

# Warning and stop if no telescope selected
#if len(telescopes) == 0:
 #   st.markdown('## Please select at least one telescope')

#else:


# Markdown section to display instructions
st.markdown("## Average length of stay by Year and Country 🏡")
#st.markdown("## Select Countries")
#st.markdown("Please select one or more countries from the list below:")
selected_countries = st.multiselect("Select Countries", df1['Entity'].unique())
filtered_df1 = df1[df1['Entity'].isin(selected_countries)]
#st.write("### Selected Data")
#st.write(filtered_df)
if not filtered_df1.empty:
    fig = px.line(filtered_df1, x='Year', y='Average length of stay', color='Entity', title='Average length of stay by Year and Country',labels={'Entity': 'Country'})
    st.plotly_chart(fig)
else:
    st.write("No data available for the selected countries.")


# Markdown section to display instructions
#st.markdown('##Average Expenditure by Year and Country')
st.markdown("## Average Expenditure by Year and Country 💲")
#st.markdown("Please select one or more countries from the list below:")
selected_countries = st.multiselect("Select Countries", df2['Entity'].unique())
filtered_df2 = df2[df2['Entity'].isin(selected_countries)]
#st.write("### Selected Data")
#st.write(filtered_df2)
if not filtered_df2.empty:
    fig = px.line(filtered_df2, x='Year', y='Outbound Tourism Expenditure (adjusted for US 2021 inflation)', color='Entity', title='Average Expenditure by Year and Country', labels={'Entity': 'Country'})
    st.plotly_chart(fig)
else:
    st.write("No data available for the selected countries.")

