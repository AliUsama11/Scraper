import requests
from bs4 import BeautifulSoup

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

# Print the dates
print("Birth Date:", birth_date)
print("Death Date:", death_date)
