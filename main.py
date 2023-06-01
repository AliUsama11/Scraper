import streamlit as st
from bs4 import BeautifulSoup
import requests

def scrape_specific_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the specific element(s) you want to scrape
    # Replace 'element_tag' with the HTML tag of the specific element
    specific_elements = soup.find_all('element_tag')

    # Extract the desired data from the specific elements
    scraped_data = [element.text for element in specific_elements]

    return scraped_data

# Streamlit app layout
st.set_page_config(layout="wide")
st.title("Specific Data Scraping App")

# Sidebar
st.sidebar.title("Settings")
url = st.sidebar.text_input("Enter the URL to scrape")
search_query = st.sidebar.text_input("Enter the search query")

# Main content area
if st.sidebar.button("Scrape"):
    if url and search_query:
        scraped_data = scrape_specific_data(url)
        filtered_data = [data for data in scraped_data if search_query.lower() in data.lower()]
        if filtered_data:
            st.write("Scraped Data:")
            for data in filtered_data:
                st.write(data)
        else:
            st.warning("No matching data found.")
    else:
        st.warning("Please enter a valid URL and search query.")
