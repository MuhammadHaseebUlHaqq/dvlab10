import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import altair as alt

st.set_page_config(page_title="Gapminder Dashboard", layout="wide")

st.title("Gapminder Data Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv('gapminder_full.csv')
    return df

df = load_data()

st.header("1. Continent-Wise Comparison")

continent_stats = df.groupby('continent').agg({
    'population': 'sum',
    'gdp_cap': 'mean',
    'life_exp': 'mean'
}).reset_index()

continent_stats.columns = ['continent', 'Total Population', 'Avg GDP per Capita', 'Avg Life Expectancy']

metric = st.selectbox(
    "Select Metric to Compare",
    ['Total Population', 'Avg GDP per Capita', 'Avg Life Expectancy']
)

fig1 = px.bar(
    continent_stats,
    x='continent',
    y=metric,
    title=f'{metric} by Continent',
    color='continent',
    text=metric
)
fig1.update_traces(texttemplate='%{text:.2s}', textposition='outside')
fig1.update_layout(showlegend=False, height=500)
st.plotly_chart(fig1, use_container_width=True)

st.header("2. GDP per Capita vs Life Expectancy")

year_filter = st.slider(
    "Select Year",
    int(df['year'].min()),
    int(df['year'].max()),
    int(df['year'].max())
)

df_filtered = df[df['year'] == year_filter]

chart = alt.Chart(df_filtered).mark_circle(size=100).encode(
    x=alt.X('gdp_cap:Q', title='GDP per Capita', scale=alt.Scale(type='log')),
    y=alt.Y('life_exp:Q', title='Life Expectancy'),
    color=alt.Color('continent:N', title='Continent'),
    size=alt.Size('population:Q', title='Population'),
    tooltip=['country', 'gdp_cap', 'life_exp', 'population', 'continent']
).properties(
    width=800,
    height=500,
    title=f'GDP per Capita vs Life Expectancy ({year_filter})'
).interactive()

st.altair_chart(chart, use_container_width=True)

st.header("3. Population Trend by Continent")

continent_year = df.groupby(['continent', 'year']).agg({
    'population': 'sum'
}).reset_index()

fig3 = px.line(
    continent_year,
    x='year',
    y='population',
    color='continent',
    title='Population Trend by Continent Over Time',
    markers=True
)
fig3.update_layout(
    xaxis_title='Year',
    yaxis_title='Total Population',
    height=500,
    hovermode='x unified'
)
st.plotly_chart(fig3, use_container_width=True)

st.header("Dataset Overview")
st.write(f"Total Records: {len(df)}")
st.write(f"Countries: {df['country'].nunique()}")
st.write(f"Years: {df['year'].min()} - {df['year'].max()}")
st.write(f"Continents: {', '.join(df['continent'].unique())}")

with st.expander("View Raw Data"):
    st.dataframe(df)

