import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Interact with Gapminder Data")

df = pd.read_csv("gapminder_tidy.csv")
metric_labels = {'gdpPercap' : 'GDP Per Capita', 'lifeExp': 'Average Life Expectancy', 'pop': 'Population'}
continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())

with st.sidebar:
    st.subheader("Configure the plot")
    continent = st.selectbox(label = "Choose a continent", options = continent_list)
    metric = st.selectbox(label = "Choose a metric", options = metric_list, format_func = lambda x: metric_labels[x])


title = f'{metric_labels[metric]} for Countries in {continent}'
labels = {'value':f'{metric_labels[metric]}', 'year':'Year','country':'Country'}

query_text = f"continent=='{continent}' & metric=='{metric}'"


df_pop_o = df.query(query_text)
fig = px.line(df_pop_o, x ='year',y='value',color ='country',title=title,labels = labels)

st.plotly_chart(fig)
