# Web_Scrapper
This Python script allows you to compare the prices of products on Flipkart and Amazon by extracting the product name and price from the given URLs. It uses web scraping techniques and libraries such as requests and BeautifulSoup to fetch the product information. The script then compares the prices and displays the results.

## How to Use
1. Make sure you have Python installed on your system.

2. Install the required libraries by running:
- pip install requests
- pip install beautifulsoup4

3. Run the script by executing it in your Python environment.
- python price_comparison.py

4. Enter the URLs of the products you want to compare on Flipkart and Amazon when prompted.

5. The script will fetch the product name and price for both websites and compare the prices.

## Script Functions
The script consists of the following functions:

- get_product_name(url, website): Retrieves the product name from the provided URL on either Flipkart or Amazon.

- get_product_price(url, website): Retrieves the product price from the provided URL on either Flipkart or Amazon.

- compare_prices(flipkart_url, amazon_url): Compares the prices of products from Flipkart and Amazon and displays the results.

## Error Handling
The script includes error handling for cases where the URLs are invalid or if there are any issues with fetching the data from the websites.

## Disclaimer
This script relies on web scraping techniques, and websites may change their structure or terms of use. Please use this script responsibly and be aware of the website's terms and conditions. It's important to respect the policies of the websites you are scraping data from.
