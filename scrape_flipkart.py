import requests
from bs4 import BeautifulSoup

# Define the website URL to scrape
url = "https://www.flipkart.com/search?q=iphone"

# Define the user agent to simulate a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Send a request to the website and get the HTML response
response = requests.get(url, headers=headers)

# Use Beautiful Soup to parse the HTML response
soup = BeautifulSoup(response.text, 'html.parser')

# Define a list to store the scraped data
data = []

# Define the CSS selector for the product names
name_selector = "._3wU53n"

# Define the CSS selector for the product prices
price_selector = "._1vC4OE._2rQ-NK"

# Loop through each product on the page and extract the name and price
for product in soup.select('.bhgxx2.col-12-12'):
    name = product.select(name_selector)[0].get_text()
    price = product.select(price_selector)[0].get_text()
    data.append({'name': name, 'price': price})

# Print the scraped data
print(data)
