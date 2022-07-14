# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.vacancy3105
    def process_item(self, item, spider):
        if spider.name == 'hhru':
            item['salary_min', 'salary_max', 'currency'] = self.process_salary(item['salary'])
            item['salary_type'] = self.process_salary(item['salary'])[3]
            collection = self.mongobase[spider.name]
            collection.insert_one(item)
        else:
            item['salary_min', 'salary_max', 'currency'] = self.process_salary_sj(item['salary'])
            collection = self.mongobase[spider.name]
            collection.insert_one(item)
        return item

    def process_salary(self, salary):
        if salary == ['з/п не указана']:
            min_s = max_s = curr = salary_type = 'no_info'
        elif salary[0] == 'от ' and salary[2] == ' до ':
            min_s = int(salary[1].replace('\xa0',''))
            max_s = int(salary[3].replace('\xa0', ''))
            curr = salary[5]
            salary_type = salary[-1]
        elif salary[0] == 'от ' and salary[2] != ' до ':
            min_s = int(salary[1].replace('\xa0', ''))
            max_s = 'no_info'
            curr = salary[3]
            salary_type = salary[-1]
        elif salary[0] == 'до ':
            min_s =  'no_info'
            max_s = int(salary[1].replace('\xa0', ''))
            curr = salary[3]
            salary_type = salary[-1]
        return min_s, max_s, curr, salary_type

    def process_salary_sj(self, salary):
        if salary == ['По договорённости']:
            min_s = max_s = curr = 'no_info'
        elif salary[0] == 'от':
            min_s_cur = salary[2].replace('\xa0', '')
            min_s = int(''.join(x for x in min_s_cur if x.isdigit()))
            max_s = 'no_info'
            curr = ''.join(x for x in min_s_cur if x.isalpha())
        elif salary[0] == 'до':
            min_s = 'no_info'
            max_s_cur = salary[2].replace('\xa0', '')
            max_s = int(''.join(x for x in max_s_cur if x.isdigit()))
            curr = ''.join(x for x in max_s_cur if x.isalpha())
        else:
            min_s = int(salary[0].replace('\xa0', ''))
            max_s = int(salary[1].replace('\xa0', ''))
            curr = salary[3]
        return min_s, max_s, curr
