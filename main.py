import requests
from bs4 import BeautifulSoup


def parse(url):
    request = requests.get(url).text
    soup = BeautifulSoup(request,'html.parser')
    box = soup.find('div',class_='row')
    cold = box.find('div',class_='col-md-3')
    mb_25 = cold.find('div',class_='mb-25')
    info = mb_25.findAll('a',class_='news-lenta')
    for news in info:
        news_time = news.find('div',class_='news-meta').find('span').get_text(strip=True)
        news_text = news.find('span',class_='news-lenta__title').get_text(strip=True)
        return f'{news_time} : {news_text}'



url = parse('https://kun.uz/')

print(url)