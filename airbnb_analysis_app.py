import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit_option_menu
from matplotlib import pyplot as plt
import seaborn as sns


# Function to load data
def load_data():
    return pd.read_csv('C:\\Users\\DIVAHAR\\PycharmProjects\\P18_1\\airbnb\\Airbnb.csv')


# Function for geographical visualization with a globe map
def geovisuals():

    df = load_data()

    # Create a choropleth map using Plotly Express
    location = px.choropleth(data_frame=df,
                             locations='country',
                             color='country',
                             hover_data={'price': True, 'rating': True, 'availability_365': True,
                                         'property_type': True},
                             locationmode='country names')
    st.header(":orange[Geo Visualization of Airbnb Data:]")
    # Customize the layout of the chart
    location.update_layout(autosize=False, margin=dict(l=10, r=0, b=20, t=20, pad=9, autoexpand=True), width=1000, )
    # Display the Plotly chart
    st.plotly_chart(location)


# Function for creating plots and charts
def plots_and_charts():
    df = load_data()

    # Define titles and descriptions
    chart_info = [
        ("Property Types vs Prices", "Price distribution for different property types."),
        ("Top 100 Property Price", "Price distribution for the top 100 properties."),
        ("Top 100 Property vs Rating", "Comparison of property types with ratings for the top 100 properties."),
        ("Total Room Types", "Count of different room types."),
        ("Bed Types Available and Their Counts", "Count of bed types available."),
        ("Property Type with Rating Below 85", "Property types with ratings below 85."),
        ("Average Listing Price in Countries", "Average listing prices in different countries."),
        ("Price vs Rating", "Relationship between price and rating."),
        ("No of Days Property Available for a Year", "Availability of properties for a year."),
        ("Top 10 Property Types", "Top 10 property types with the highest listings.")
    ]

    col1, col2 = st.columns([1, 1], gap='large')
    fixed_figsize = (10, 5)

    for i, (title, description) in enumerate(chart_info):
        with col1 if i % 2 == 0 else col2:
            st.title(title)
            st.markdown(description)
            plt.figure(figsize=fixed_figsize)
            if i == 0:
                x = sns.barplot(data=df, y=df['property_type'], x=df['price'])
            elif i == 1:
                x = sns.violinplot(x=df['price'].head(100))
            elif i == 2:
                x = sns.boxplot(data=df, y=df['property_type'].head(100), x=df['rating'].head(100))
            elif i == 3:
                x = sns.countplot(data=df, y=df['room_type'])
            elif i == 4:
                x = sns.countplot(data=df, x=df['bed_type'], order=df['bed_type'].value_counts().index[1:10])
            elif i == 5:
                x = sns.barplot(data=df, y=df['property_type'][df['rating'] < 85], x=df['rating'][df['rating'] < 85])
            elif i == 6:
                country_df = df.groupby('country', as_index=False)['price'].mean()
                plt.figure(figsize=fixed_figsize)
                x = sns.scatterplot(data=country_df, y=country_df['price'], x=country_df['country'])
            elif i == 7:
                x = sns.barplot(data=df, x=df['rating'], y=df['price'])
            elif i == 8:
                x = sns.barplot(data=df, y=df['property_type'], x=df['availability_365'])
            elif i == 9:
                x = sns.countplot(data=df, y=df['property_type'],
                                  order=df['property_type'].value_counts().iloc[:10].index)

            # Display the chart in the Streamlit app
            st.pyplot(x.get_figure(), use_container_width=True)


# Main Streamlit application
def main():
    st.set_page_config(layout="wide", page_title="Airbnb Analysis")

    selected = streamlit_option_menu.option_menu(
        "Menu",
        ["About", "Plots and Charts", "GeoVisualization", 'Contact'],
        icons=["exclamation-circle", "bar-chart", "globe", 'telephone-forward'],
        menu_icon="menu-button-wide",
        default_index=0,
        orientation="horizontal",
        styles={"nav-link": {"font-size": "15px", "text-align": "centre", "--hover-color": "#d1798e"},
                "nav-link-selected": {"background-color": "#b30e35"}}
    )

    if selected == 'About':
        st.title(':red[Project Title: Airbnb Analysis]')
        st.header(':red[ Technologies used:]')
        st.subheader('Python scripting, Data Preprocessing, Visualization, EDA, Streamlit, MongoDB, PowerBI or Tableau')
        st.header(':red[  Domain:]')
        st.subheader('Travel Industry, Property Management, and Tourism')
        st.title(':red[ About Application:]')
        st.markdown('''
         As an Airbnb host or potential host, you may have wondered about the factors that affect rental prices and occupancy rates on the platform. By analyzing Airbnb data, we can gain insights into these trends and make data-driven decisions to maximize your earning potential.
         One key aspect to consider is the location of your property. By examining data from different neighborhoods or cities, we can determine which areas have higher demand and corresponding higher prices. For example, properties near popular tourist attractions, city centers, or major transportation hubs tend to have higher occupancy rates and rental prices.
         Another factor that influences rental prices is the type of property you offer. By analyzing data on different accommodation types, such as entire homes, private rooms, or shared spaces, you can identify which options are in higher demand and can potentially fetch higher prices. Understanding the preferences of Airbnb users can guide your decision-making and help you optimize your listing.
         Additionally, analyzing historical booking data can provide insights into seasonal demand patterns. By examining trends across different months or even specific events or holidays, you can determine the optimal time to list your property and adjust prices accordingly. This can help maximize your rental income and achieve higher occupancy rates throughout the year.
         Moreover, guest reviews play a crucial role in attracting potential guests. Analyzing review data can provide insights into the factors that contribute to positive guest experiences, such as cleanliness, responsiveness, and amenities. Understanding these preferences can help you improve your listing and enhance guest satisfaction, leading to positive reviews and increased bookings.
         Lastly, analyzing data on similar listings in your area can help you set competitive prices. By examining the rental prices and occupancy rates of comparable properties, you can ensure that your listing is competitive and attractive to potential guests.
         In conclusion, analyzing Airbnb data can provide valuable insights into various factors that affect rental prices and occupancy rates. By leveraging this data, hosts can make informed decisions to optimize their listings, maximize earning potential, and provide exceptional guest experiences.
        ''')

    if selected == 'Plots and Charts':
        plots_and_charts()

    if selected == 'GeoVisualization':
        geovisuals()

    if selected == 'Contact':
        st.subheader("Contact Information")
        st.write("Name: Divahar Murugan")
        st.write("Email: divahar2896@gmail.com")


if __name__ == '__main__':
    main()
