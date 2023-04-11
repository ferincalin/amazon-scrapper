import requests
from bs4 import BeautifulSoup

# Define the URL you want to scrape
url = 'https://www.amazon.com/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find and extract the relevant data using BeautifulSoup's methods
# Example: extract the titles of all products on the page
product_titles = []
for product in soup.find_all('div', {'class': 'product-title'}):
    title = product.text.strip()
    product_titles.append(title)

# Save the extracted data to a file or database
# Example: save the product titles to a CSV file
import csv

with open('product_titles.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title'])
    for title in product_titles:
        writer.writerow([title])
