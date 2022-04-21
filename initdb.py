import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

url = 'http://www.befreetour.com/'

client = MongoClient('localhost', 27017)
db = client.dbsparta

def insert_tour():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    print(soup)

    tours = soup.select('body > div.container.margin_60 > div:nth-child(5) > div')
    for tour in tours:
        title = tour.select_one('div > a > div.act_title > h3').text
        image = tour.select_one('div > a > div.act_img_container')['style']
        image_split = image.split('(', 1)[1]
        image_split1 = image_split.split(')', 1)[0]
        price = tour.select_one('div > a > div.act_title > div > span.act_price').text.split('₩', 1)[1].strip()
        doc = {'title': title,
               'image': image_split1,
               'price': price,
               'like': 0}

        db.tour.insert_one(doc)

insert_tour()