# 📊 India Data Explorer

India Data Explorer is a Streamlit web application that provides interactive visualizations of various demographic parameters for states and districts in India.

[Deploy Link](https://india-data-explorer-ds9wspo7doe88dzgadsdyk.streamlit.app/)

## Overview

India Data Explorer allows users to explore demographic data such as population, literacy rate, sex ratio, internet access, and electricity access across different states and districts of India. Users can select different parameters and visualize the data on an interactive map along with additional graphs for detailed insights.

## Features

- Interactive sidebar for parameter selection
- Dynamic visualization updates based on user input
- Geographic visualization using Plotly's scatter mapbox
- Additional graphs including bar charts and pie charts for deeper analysis
- Detailed statistics including maximum and minimum values for selected parameters
- User-friendly interface with customization options

## How to Use

1. **Select Parameters**: Use the sidebar to select a state, primary parameter, and secondary parameter.
2. **Plot Graph**: Click the "Plot Graph" button to visualize the data.
3. **Explore**: Interact with the map and additional graphs to explore demographic trends.
4. **Detailed Statistics**: View maximum and minimum values for selected parameters.

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Gorachand22/India-Data-Explorer.git
```

2.Install the required dependencies:

```bash
pip install -r requirements.txt
```

3.Run the Streamlit application:

```bash
streamlit run app.py
```

4.Access the application in your browser at `http://localhost:8501`.

## Data Source

The demographic data used in this application is sourced from [data/india.csv](data/india.csv).

## Technologies Used

- Streamlit
- Plotly Express
- Pandas
- Python

## About the Author

This project is maintained by [Gorachanda Dash](https://github.com/Gorachand22). Feel free to reach out with any questions or suggestions!
