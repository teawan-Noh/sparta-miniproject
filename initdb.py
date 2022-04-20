import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

url = 'http://www.befreetour.com/'

client = MongoClient('localhost', 27017)
db = client.dbsparta


# 출처 url로부터 영화인들의 사진, 이름, 최근작 정보를 가져오고 mystar 콜렉션에 저장합니다.
def insert_tour():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    tours = soup.select('body > div.container.margin_60 > div:nth-child(5) > div')
    for tour in tours:
        title = tour.select_one('div > a > div.act_title > h3').text
        image = tour.select_one('div > a > div.act_img_container')['style']
        image_split = image.split('(', 1)[1]
        image_split1 = image_split.split(')', 1)[0]
        price = tour.select_one('div > a > div.act_title > div > span.act_price').text.split('₩', 1)[1].strip()
        doc = {'title': title,
               'image': image_split1,
               'price': price}

        db.tours.insert_one(doc)


### 실행하기
insert_tour()