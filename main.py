import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_allama_iqbal_dates():
    url = "https://example.com/allama-iqbal"  # Replace with the actual URL of the webpage containing the information

    # Fetch the webpage content
    response = requests.get(url)
    html_content = response.content

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the elements containing birth and death dates
    birth_date_element = soup.find("span", {"class": "birth-date"})
    death_date_element = soup.find("span", {"class": "death-date"})

    # Extract the dates
    birth_date = birth_date_element.text.strip() if birth_date_element else "N/A"
    death_date = death_date_element.text.strip() if death_date_element else "N/A"

    return birth_date, death_date

# Streamlit app
st.title("Allama Iqbal Birth and Death Dates")

# Scrape the dates
birth_date, death_date = scrape_allama_iqbal_dates()

# Display the dates on Streamlit
st.write("Birth Date:", birth_date)
st.write("Death Date:", death_date)
