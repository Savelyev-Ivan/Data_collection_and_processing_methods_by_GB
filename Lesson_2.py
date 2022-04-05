import re

from bs4 import BeautifulSoup as bs
import requests
from  pprint import pprint

url = 'https://yandex.ru'

responce = requests.get(url)

dom = bs(responce.text, 'html.parser')

tag_a = dom.find('a')
#pprint(tag_a)

parent_a = tag_a.parent
#pprint(parent_a)

#children_div = list(parent_a.children)
children_div = parent_a.findChildren(recursive=False)
#pprint(children_div)
#pprint(len(children_div))

#div_d = dom.find('div', {'id': 'd'}
#pprint(div_d)

tags_p = dom.find_all('ol', {'class': 'news__list'})
pprint(tags_p)

#p6 = dom.find(text='Макрон заявил Путину о невозможности платить за газ в рублях')
p7 = dom.find(lambda tag: tag.string and re.search(r'Путин', tag.string.text))
pprint(p7)