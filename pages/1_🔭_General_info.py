"""
General information about the mission. 
By default, all telescopes are selected.
For each one, it charges the image with the logo, and then read the text written in the 
utils/general_description dictionary.
The dictionary is formatted with sub dictionary:
For each telescope name, you have a key for the Instruments and the Surveys. This way, we can
loop through the information, have a standardized format and an easier readability of the dictionary.

"""


import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import plotly.express as px
import sys
from telescopes.main_info import info
from utils.general_description import description

# Load your DataFrame
df = pd.read_csv('/workspaces/SurViZ/data/tourism dataset power bi.csv')

# Sidebar multiselects for user instructions
st.sidebar.markdown("## Select Filters")
selected_age_groups = st.sidebar.multiselect("Select Age Groups", df['age_group'].unique())
selected_countries = st.sidebar.multiselect("Select Countries", df['country'].unique())
selected_main_activities = st.sidebar.multiselect("Select Main Activities", df['main_activity'].unique())

# Filter DataFrame based on selected values
filtered_df = df[
    (df['age_group'].isin(selected_age_groups)) &
    (df['country'].isin(selected_countries)) &
    (df['main_activity'].isin(selected_main_activities))
]

# Default plots
st.subheader("Default Plots")

# Plot horizontal bar graph of total_tourists vs purpose
default_bar_fig = px.bar(df, y='purpose', x='Sum of Total_tourists', orientation='h',
                         title='Total Tourists vs Purpose (Default)', 
                         labels={'purpose': 'Purpose', 'Sum of Total_tourists': 'Total Tourists'})
st.plotly_chart(default_bar_fig)

# Plot pie chart of info_source vs Sum of Total_tourists
default_pie_fig = px.pie(df, values='Sum of Total_tourists', names='info_source', 
                         title='Information Source vs Sum of Total Tourists (Default)')
st.plotly_chart(default_pie_fig)

# Update plots based on user selections
st.subheader("Updated Plots")

# Check if there are any selections made
if selected_age_groups or selected_countries or selected_main_activities:
    # Plot horizontal bar graph of total_tourists vs purpose based on user selections
    if not filtered_df.empty:
        bar_fig = px.bar(filtered_df, y='purpose', x='Sum of Total_tourists', orientation='h',
                         title='Total Tourists vs Purpose (Updated)', 
                         labels={'purpose': 'Purpose', 'Sum of Total_tourists': 'Total Tourists'})
        st.plotly_chart(bar_fig)
    else:
        st.write("No data available for the selected filters.")

    # Plot pie chart of info_source vs Sum of Total_tourists based on user selections
    pie_fig = px.pie(filtered_df, values='Sum of Total_tourists', names='info_source', 
                     title='Information Source vs Sum of Total Tourists (Updated)')
    st.plotly_chart(pie_fig)
else:
    st.write("Make selections to see updated plots.")