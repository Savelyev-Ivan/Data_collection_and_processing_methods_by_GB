from bs4 import BeautifulSoup as bs
import pandas as pd
import requests



main_url = 'https://hh.ru/'

params = {'search_field': ['name', 'company_name', 'description']}
params['text'] = input('Введите вакансию для поиска: ')
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
page_link = '/search/vacancy'
vacancies = []
i = 0

def salary(salary_vacancy):
    dict_salary = {'min': None, 'max': None, 'cur': None}

    if salary_vacancy:
        salary_raw = salary_vacancy.getText().replace(' – ', ' ').replace(' ', '').split()
        if salary_raw[0] == 'до':
            dict_salary['max'] = int(salary_raw[1])
        elif salary_raw[0] == 'от':
            dict_salary['min'] = int(salary_raw[1])
        else:
            dict_salary['min'] = int(salary_raw[0])
            dict_salary['max'] = int(salary_raw[1])
        dict_salary['cur'] = salary_raw[2].replace('.', '')

    return dict_salary

while True:
    response = requests.get(main_url + page_link,
                            params=params,
                            headers=headers)
    html = response.text
    soup = bs(html, 'html.parser')
    vacancies_soup = soup.find_all('div', {'class': ['vacancy-serp-item-body__main-info']})

    for vacancy in vacancies_soup:

        vacancy_data = {'website': 'hh.ru'}

        vacancy_title = vacancy.find('a')

        vacancy_name = vacancy_title.getText()
        link = vacancy_title['href'][: vacancy_title['href'].index('?')]
        salary_vacancy = salary(vacancy.find('span', {'class': ['bloko-header-section-3']}))
        employer = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).getText().replace('\xa0', ' ')
        address = vacancy.find('div', {'data-qa': 'vacancy-serp__vacancy-address'}).getText().replace('\xa0', ' ')

        vacancy_data['name'] = vacancy_name
        vacancy_data['link'] = link
        vacancy_data['salary_min'] = salary_vacancy['min']
        vacancy_data['salary_max'] = salary_vacancy['max']
        vacancy_data['salary_currency'] = salary_vacancy['cur']
        vacancy_data['employer'] = employer
        vacancy_data['address'] = address

        vacancies.append(vacancy_data)

    next_page = soup.find('a', {'data-qa': 'pager-next'})
    if not next_page:
        break
    page_link = next_page['href']
    i += 1

vacancies_data = pd.DataFrame(data=vacancies)
prefix = '_'.join(params['text'].split())
vacancies_data.to_csv(f'{prefix}_hh_vacancies.csv', index=False)