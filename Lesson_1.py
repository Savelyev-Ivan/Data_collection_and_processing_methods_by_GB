import requests

url = 'https://www.google.ru'

response = requests.get(url)
# if response.status_code == 200:
#    pass

if response.ok:
    pass

response.headers['Content-Type']
print()

response.text
response.content
response.url

