from lxml import html
import requests
from pprint import pprint
url = 'https://ru.ebay.com/b/Wristwatches/31387/bn_2408451'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'}
response = requests.get(url, headers=header)

dom = html.fromstring(response.text)

watchs_list = dom.xpath("//li[contains(@class,'s-item')]")
watchs = []
for watch in watchs_list:
    watch_info = {}
    names = watch.xpath("//h3[@class='s-item__title']/text()")
    links = watch.xpath("//h3[@class='s-item__title']/../@href")
    price = watch.xpath("//span[@class='s-item__price']//text()")
    info = watch.xpath("//span[@class='s-item__hotness s-item__itemHotness']//text()")

    watch_info['name'] = names[0]
    watch_info['links'] = links[0]
    watch_info['price'] = price
    watch_info['info'] = info
    watchs.append(watch_info)
pprint(watchs)
