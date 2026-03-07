import streamlit as st
from dbhelper import DB
import plotly.graph_objs as go


db = DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['Select one', 'Check Flights', 'Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')

    col1, col2 = st.columns(2)

    city = db.fetch_city_names()

    with col1:
     source = st.selectbox('source_city', sorted(city))
    with col2:
     destination = st.selectbox('destination_city', sorted(city))
    if st.button('Search'):
        results = db.fetch_all_flights(source, destination)
        st.dataframe(results)
elif user_option == 'Analytics':
    airline,frequency = db.fetch_airline_frequency()
    st.title("Airline Market Share")
    fig = go.Figure(
        data=[
            go.Pie(
                labels=airline,
                values=frequency,
                hoverinfo="label+percent",
                textinfo="value"
            )
        ]
    )
    st.plotly_chart(fig)


    city, frequency = db.busy_airport()

    fig = go.Figure(
        data=[
            go.Bar(
                x=city,  # X-axis → cities
                y=frequency,  # Y-axis → frequency
                text=frequency,  # show values on bars
                textposition='auto'
            )
        ]
    )

    fig.update_layout(
        title="Busiest Airports",
        xaxis_title="City",
        yaxis_title="Number of Flights"
    )
    st.plotly_chart(fig)


else:
    st.title('tell about the project')