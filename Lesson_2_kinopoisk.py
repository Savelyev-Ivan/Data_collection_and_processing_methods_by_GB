# https://www.kinopoisk.ru/lists/movies/popular-series/?b=series
from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

main_url = 'https://www.kinopoisk.ru'
params = {'b': 'series'}
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}
#response = requests.get(main_url+'/lists/movies/popular-series/', params=params, headers=headers)
#with open('page.html', 'w', encoding='utf-8') as f:
#     f.write(response.text)
html = ''
with open('page.html', 'r',  encoding='utf-8') as f:
    html = f.read()

soup = bs(html, 'html.parser')

serials = soup.find('main').findChildren(recursive=False)
print(len(serials))

all_serials = []
for serial in serials[2:5]:
     serial_info = {}
     serial_anchor = serial.find_all('span')[1]
     serial_name = serial_anchor.getText()
     serial_anchor = serial_anchor.parent.parent
     serial_link = main_url + serial_anchor['href']
     serial_data = serial_anchor.findChildren(recursive=False)[2].getText().replace('\xa0', ' ')
     serial_anchor = serial_anchor.parent.nextSibling
     serial_rating = serial_anchor.find('span').getText()

     serial_info['name'] = serial_name
     serial_info['link'] = serial_link
     serial_info['data'] = serial_data
     serial_info['rating'] = serial_rating

     all_serials.append(serial_info)
pprint(serial_info)
