import requests
import json

import sys

sys.path.insert(0, 'bs4.zip')
from bs4 import BeautifulSoup

# Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs, product_glomark):
    # TODO: Aquire the web pages which contain product Price
    html = requests.get(product_laughs).content
    soup = BeautifulSoup(html, 'html.parser')
    item = soup.find('div', attrs={"class": "product-name"})
    product_name_laughs = item.h1.text

    html1 = requests.get(product_glomark).content
    soup1 = BeautifulSoup(html1, 'html.parser')
    item1 = soup1.find('div', attrs={"class": "product-title"})
    product_name_glomark = item1.h1.text

    # TODO: Laughs Super supermarket website provides the price in a
    html2 = requests.get(product_laughs).content
    soup2 = BeautifulSoup(html2, 'html.parser')
    price = soup2.find('span', attrs={"class": "regular-price"})
    price_laughs = price.span.get_text()
    price_laughs = price_laughs.replace("Rs.", "")

    price_laughs = float(price_laughs)

    # TODO: Glomark supermarket website provides the data in jason format in an inline script.
    # You can use the json module to extract only the price
    soup = BeautifulSoup(requests.get(product_glomark).content, "html.parser")
    s = soup.select_one('script[type="application/ld+json"]')
    data = json.loads(s.text)
    h = f'{data["offers"]}'
    string2 = h.split(",")
    abc = string2[1].split(":")[1]
    price = ""
    for s in abc:
        if s.isdigit():
            price = price + s
    price = int(price)

    price_glomark = float(price)

    print('Laughs  ', product_name_laughs[0:7], 'Rs.: ', price_laughs)
    print('Glomark ', product_name_glomark, 'Rs.: ', price_glomark)

    if price_laughs > price_glomark:
        print('Glomark is cheaper Rs.:', price_laughs - price_glomark)
    elif price_laughs < price_glomark:
        print('Laughs is cheaper Rs.:', price_glomark - price_laughs)
    else:
        print('Price is the same')

laughs_coconut = 'https://scrape-sm1.github.io/site1/COCONUT%20market1super.html'
glomark_coconut = 'https://glomark.lk/coconut/p/11624'

compare_prices(laughs_coconut,glomark_coconut)