#1. Посмотреть документацию к API GitHub,
# разобраться как вывести список наименований репозиториев для конкретного пользователя,
# сохранить JSON-вывод в файле *.json.
import requests
import json

#Получение списка репозиториев пользователя на гигхабе
def users_repo(username):

    url = 'https://api.github.com/users/' + username + '/repos'
    try:
        data = requests.get(url)
    except Exception:
        print('Что-то пошло не так...')
        return None
    if data.status_code == 200:
        return json.loads(data.text)
    else:
        print(f'Сервер отвечает ошибкой {data.status_code}')
        return None



user = 'Savelyev-Ivan'
data_json = users_repo(user)

if data_json:
    for item in data_json:
        print(item['name'])
    with open(f'{user}_repos.json', 'w') as f:
        f.write(json.dumps(data_json))
else:
    print('Data is None')