import requests
from bs4 import BeautifulSoup
def get_product_name(url, website):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx errors
        soup = BeautifulSoup(response.content, 'html.parser')

        if website == 'Flipkart':
            price_name = soup.find('span', {'class': 'B_NuCI'})

        elif website == 'Amazon':
            price_name = soup.find('span', {'id': 'productTitle'})


        if price_name:
            return price_name.get_text().strip()
        else:
            return "Name not found on " + website

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
def get_product_price(url, website):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx errors
        soup = BeautifulSoup(response.content, 'html.parser')

        if website == 'Flipkart':

            price_element = soup.find('div', {'class': '_30jeq3'})
        elif website == 'Amazon':

            price_element = soup.find('span', {'class': 'a-price-whole'})

        if price_element:
            return price_element.get_text().strip()
        else:
            return "Price not found on " + website

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def compare_prices(flipkart_url, amazon_url):
    flipkart_name = get_product_name(flipkart_url, 'Flipkart')
    flipkart_price = get_product_price(flipkart_url, 'Flipkart')
    amazon_name = get_product_name(amazon_url, 'Amazon')
    amazon_price = get_product_price(amazon_url, 'Amazon')
    flipkart_price = flipkart_price.replace(',', '').replace('₹', '')
    amazon_price= amazon_price.replace(',', '').replace('.', '')
    if "Error" in flipkart_price or "Error" in amazon_price:
        print("Error occurred while fetching prices.")
    else:
        print("Product prices fetched successfully.")
        print('Flipkart product name:', flipkart_name)
        print('Flipkart product price: Rs.', flipkart_price)
        print('Amazon product name:', amazon_name)
        print('Amazon product price: Rs', amazon_price)

        if flipkart_price != "Price not found on Flipkart" and amazon_price != "Price not found on Amazon":
            if int(flipkart_price) > int(amazon_price):
                print('Amazon price is lower.')
                print('Price is Rs ' + amazon_price)
            elif int(flipkart_price) < int(amazon_price):
                print('Flipkart price is lower.')
                print('Price is Rs ' + flipkart_price)
        else:
            print('Price comparison not possible due to missing price information.')

if __name__ == "__main__":
    flipkartProductURL = input('Enter the Flipkart product URL: ')
    amazonProductURL = input('Enter the Amazon product URL: ')

    if flipkartProductURL and amazonProductURL:
        compare_prices(flipkartProductURL, amazonProductURL)
    else:
        print('Please enter valid URLs for both Flipkart and Amazon products.')
