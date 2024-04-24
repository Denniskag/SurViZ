
"""
Visualisation of the mirrors and fields of view
The user have to select the telescopes he want to display. For each selected telescope,

The mirror information are stored in the instruments file (/telescopes/telescopes.py)
For each selection, the dictionary info from /telescopes/main_info is read.
The structure is as follow. To read Euclid's FOV we read: 
    -info['Euclid]['fov']

The plotting is done by plot_mirrors and plot_fov in /utils/plot.py
"""


import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from telescopes.main_info import info
from utils.plots import plot_mirrors, plot_fovs
from telescopes.references import mirrors_refs



df = pd.read_csv('/workspaces/SurViZ/data/tourism dataset power bi.csv')
package_columns_horizontal = ['package_accomodation', 'package_food', 'package_guided_tour', 'package_insurance']
package_columns_vertical = ['package_sightseeing', 'package_transport_int', 'package_transport_tz']

# Plot count plots for all data initially
st.subheader("Count Plots (All Data)")

# Arrange plots in rows and columns
num_columns = 2

# Horizontal count plots
st.subheader("Horizontal Count Plots")
num_horizontal_plots = len(package_columns_horizontal)
num_horizontal_rows = (num_horizontal_plots + num_columns - 1) // num_columns

for i in range(num_horizontal_rows):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        idx = i * num_columns + j
        if idx < num_horizontal_plots:
            fig = px.histogram(df, x=package_columns_horizontal[idx], title=f'{package_columns_horizontal[idx].capitalize()} Distribution', labels={'count': 'Number of Tourists'})
            cols[j].plotly_chart(fig, use_container_width=True)

# Vertical count plots
st.subheader("Vertical Count Plots")
num_vertical_plots = len(package_columns_vertical)
num_vertical_rows = (num_vertical_plots + num_columns - 1) // num_columns

for i in range(num_vertical_rows):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        idx = i * num_columns + j
        if idx < num_vertical_plots:
            fig = px.histogram(df, x=package_columns_vertical[idx], title=f'{package_columns_vertical[idx].capitalize()} Distribution', labels={'count': 'Number of Tourists'})
            cols[j].plotly_chart(fig, use_container_width=True)

# Sidebar slicers for user selection
st.sidebar.markdown("## Select Filters")
selected_age_groups = st.sidebar.multiselect("Select Age Groups", df['age_group'].unique())
selected_first_trips = st.sidebar.multiselect("Select First Trips", df['first_trip_tz'].unique())
selected_main_activities = st.sidebar.multiselect("Select Main Activities", df['main_activity'].unique())

# Filter DataFrame based on selected values
filtered_df = df[
    (df['age_group'].isin(selected_age_groups)) &
    (df['first_trip_tz'].isin(selected_first_trips)) &
    (df['main_activity'].isin(selected_main_activities))
]

# Plot count plots after selection
st.subheader("Count Plots (After Selection)")

# Horizontal count plots
st.subheader("Horizontal Count Plots")
num_horizontal_plots = len(package_columns_horizontal)
num_horizontal_rows = (num_horizontal_plots + num_columns - 1) // num_columns

for i in range(num_horizontal_rows):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        idx = i * num_columns + j
        if idx < num_horizontal_plots:
            fig = px.histogram(filtered_df, x=package_columns_horizontal[idx], title=f'{package_columns_horizontal[idx].capitalize()} Distribution', labels={'count': 'Number of Tourists'})
            cols[j].plotly_chart(fig, use_container_width=True)

# Vertical count plots
st.subheader("Vertical Count Plots")
num_vertical_plots = len(package_columns_vertical)
num_vertical_rows = (num_vertical_plots + num_columns - 1) // num_columns

for i in range(num_vertical_rows):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        idx = i * num_columns + j
        if idx < num_vertical_plots:
            fig = px.histogram(filtered_df, x=package_columns_vertical[idx], title=f'{package_columns_vertical[idx].capitalize()} Distribution', labels={'count': 'Number of Tourists'})
            cols[j].plotly_chart(fig, use_container_width=True)

