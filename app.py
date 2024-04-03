import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='India Data Explorer', page_icon='📊', layout='wide')

df = pd.read_csv('data/india.csv')

list_of_states = df['State'].unique().tolist()  # list of states
list_of_states.insert(0, 'Overall India')

st.sidebar.title('Welcome to IDE')
st.sidebar.info('Use the sidebar to select different parameters')
st.info('Size represents primary parameter')
st.info('Color represents secondary parameter')

selected_state = st.sidebar.selectbox('Select a state', list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:].to_list()))
secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:].to_list()))

plot = st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'Overall India':
        column4 = st.container(height=300)
        dict = {
            'Max': {
                'Population': df['Population'].max(),
                'Households_with_Internet': df['Households_with_Internet'].max(),
                'Housholds_with_Electric_Lighting': df['Housholds_with_Electric_Lighting'].max(),
                'sex_ratio': df['sex_ratio'].max(),
                'Literacy_Rate': df['Literacy_Rate'].max(),
            },
            'Min': {
                'Population': df['Population'].min(),
                'Households_with_Internet': df['Households_with_Internet'].min(),
                'Housholds_with_Electric_Lighting': df['Housholds_with_Electric_Lighting'].min(),
                'sex_ratio': df['sex_ratio'].min(),
                'Literacy_Rate': df['Literacy_Rate'].min(),
            }
        }

        column4.data_editor(dict,use_container_width=True)

        column5 = st.container(height=500)
        # plot for India
        fig = px.scatter_mapbox(df, lat="Latitude",
                                lon="Longitude",
                                size=df[primary],
                                color=df[secondary],
                                zoom=4,
                                size_max=35,
                                mapbox_style="carto-positron",
                                width=1200,
                                height=700,
                                hover_name='District')

        column5.plotly_chart(fig, use_container_width=True)
    else:
        # plot for state
        state_df = df[df['State'] == selected_state]

        column2 = st.container(height=300)
        # Additional Graphs
        column2.header('Description for {}'.format(selected_state))
        dict = {
            'Max': {
                'Population': state_df['Population'].max(),
                'Households_with_Internet': state_df['Households_with_Internet'].max(),
                'Housholds_with_Electric_Lighting': state_df['Housholds_with_Electric_Lighting'].max(),
                'sex_ratio': state_df['sex_ratio'].max(),
                'Literacy_Rate': state_df['Literacy_Rate'].max(),
            },
            'Min': {
                'Population': state_df['Population'].min(),
                'Households_with_Internet': state_df['Households_with_Internet'].min(),
                'Housholds_with_Electric_Lighting': state_df['Housholds_with_Electric_Lighting'].min(),
                'sex_ratio': state_df['sex_ratio'].min(),
                'Literacy_Rate': state_df['Literacy_Rate'].min(),
        }
        }

        column2.data_editor(dict,use_container_width=True)

        column3 = st.container(height=500)
        # plot for state
        fig = px.scatter_mapbox(state_df, lat="Latitude",
                                lon="Longitude",
                                size=primary,
                                color='District',
                                zoom=6,
                                size_max=35,
                                mapbox_style="carto-positron",
                                width=1200,
                                height=700,
                                hover_name='District')

        column3.plotly_chart(fig, use_container_width=True)

        # Additional Graphs
        st.subheader('Additional Graphs for {}'.format(selected_state))
   
        container1 = st.container(height=500)
        container1.write('### Population Distribution')
        # Bar chart for population distribution
        fig_population = px.bar(state_df, 
                                x='District', 
                                y='Population', 
                                color='District',
                                title='Population Distribution',
                                labels={'Population': 'Population', 'District': 'District'})
        container1.plotly_chart(fig_population, use_container_width=True)
        
        col = st.columns(2)

        container2 = col[0].container(height=500)
        container2.write('### Internet Access')
        # Bar chart for Internet Access
        fig_internet = px.bar(state_df, 
                              x='District', 
                              y='Households_with_Internet', 
                              color='District',
                              title='Internet Access',
                              labels={'Households_with_Internet': 'Households_with_Internet', 'District': 'District'})
        container2.plotly_chart(fig_internet, use_container_width=True)


        container3 = col[1].container(height=500)
        container3.write('### Electricity Access')
        # Bar chart for Electricity Access
        fig_electricity = px.bar(state_df, 
                                 x='District', 
                                 y='Housholds_with_Electric_Lighting', 
                                 color='District',
                                 title='Electricity Access',
                                 labels={'Housholds_with_Electric_Lighting': 'Housholds_with_Electric_Lighting', 'District': 'District'})
        container3.plotly_chart(fig_electricity, use_container_width=True)


        column = st.columns(2)
        container4 = column[0].container(height=500)
        # Pie chart for literacy rate
        container4.write('### Literacy Rate Distribution')
        fig_literacy = px.pie(state_df, 
                              values='Literacy_Rate', 
                              names='District', 
                              title='Literacy Rate Distribution')
        container4.plotly_chart(fig_literacy, use_container_width=True)
        

        container5 = column[1].container(height=500)
        # Pie chart for sex ratio
        container5.write('### Sex Ratio Distribution')
        fig_sex_ratio = px.pie(state_df, 
                               values='sex_ratio', 
                               names='District', 
                               title='Sex Ratio Distribution')
        container5.plotly_chart(fig_sex_ratio, use_container_width=True)

