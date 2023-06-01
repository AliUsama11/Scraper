import streamlit as st
from bs4 import BeautifulSoup
import requests

def scrape_specific_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

   
    specific_elements = soup.find_all('element_tag')

    scraped_data = [element.text for element in specific_elements]

    return scraped_data

st.title("Specific Data Scraping App")
url = st.text_input("Enter the URL to scrape")

if st.button("Scrape"):
    if url:
        scraped_data = scrape_specific_data(url)
        for data in scraped_data:
            st.write(data)
    else:
        st.warning("Please enter a valid URL.")
