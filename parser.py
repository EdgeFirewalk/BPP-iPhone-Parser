from bs4 import BeautifulSoup
import requests

# Eldorado returns status code 503
# DNS returns some kind of encrypted page
# Citilink works fine so I'm parsing it

def parse():
    url = 'https://www.citilink.ru/catalog/smartfony/APPLE'
    page = requests.get(url)
    print("Status code: " + str(page.status_code))
    soup = BeautifulSoup(page.text, "html.parser")
    
    block = soup.findAll('span', class_='ProductCardHorizontal__price_current-price js--ProductCardHorizontal__price_current-price')
    prices = []
    for data in block:
        prices.append(int(str(data.text).replace(' ', '').replace('\n', '')))
    print("iPhones found: " + str(len(prices)))

    print("---")
    print("Max price: " + str(max(prices)))
    print("Min price: " + str(min(prices)))
    print("Average: " + str(sum(prices) / len(prices)))

parse()
