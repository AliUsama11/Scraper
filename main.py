import streamlit as st
from bs4 import BeautifulSoup
import requests

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = [title.string for title in soup.find_all('title')]
    paragraphs = [p.text for p in soup.find_all('p')]
    return titles, paragraphs

st.title("Data Scraping App")
url = st.text_input("Enter the URL to scrape")

if st.button("Scrape"):
    if url:
        titles, paragraphs = scrape_data(url)
        st.write("Titles:")
        for title in titles:
            st.write(title)
       
        st.write("Paragraphs:")
        for paragraph in paragraphs:
            st.write(paragraph)
    else:
        st.warning("Please enter a valid URL.")
