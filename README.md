# dvlab10

## Gapminder Data Dashboard

A Streamlit dashboard for visualizing Gapminder dataset with interactive charts.

### Features

- **Bar Chart**: Continent-wise comparison of Population, GDP per Capita, and Life Expectancy
- **Scatter Plot**: GDP per Capita vs Life Expectancy with year slider
- **Line Chart**: Population trends by continent over time

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
python -m streamlit run dashboard.py
```

### Dataset

The dashboard uses the Gapminder dataset (`gapminder_full.csv`) containing:
- Country-level data from 1952 to 2007
- Population, GDP per capita, Life expectancy metrics
- Coverage across 5 continents

### Technologies

- Streamlit
- Plotly
- Altair
- Pandas

