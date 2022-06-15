from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import DuplicateKeyError as dke

client = MongoClient('127.0.0.1', 27017)

db = client['users2005']

persons = db.persons

#doc = {'autor': 'Ivan',
#       "age": 35,
#       "text": "Cool! Wilberry",
#       "tags": ['cool', 'hot', 'ice'],
#       "date": '14.06.1984'}

#doc1 = {"_id": 88000000001,
#        'autor': 'Ivan',
#       "age": 35,
#       "text": "Cool! Wilberry",
#       "tags": ['cool', 'hot', 'ice'],
#       "date": '14.06.1984'}

#try:
#    persons.insert_one(doc1)
#except dke:
#    print(f'Document this id was created early')

#authors_list = ([{'autor': 'Mark',
#       "age": 36,
#       "text": "Too bad! Strawbbery",
#       "tags": 'ice',
#       "date": '10.04.1972'},
#        {"_id": 123,
#        'autor': 'Colin',
#       "age": 22,
#       "title": "Hot Cool!!!",
#       "text": 'easy too',
#       "date": '11.02.1995'},
#        {'autor': 'Jane',
#       "age": 23,
#       "title": "Nice book",
#       "text":"Pretty text not long",
#       "date": '10.04.1972',
#        "tags": ['Fantastic','criminal']}])


#for i in range(len(authors_list)):
#     try:
#        persons.insert_one(authors_list[i])
#     except dke:
#        print(f'Сломались на {i} элементе. Уже существует в базе')


#for doc in persons.find({}):
#    pprint(doc)

#result = persons.find({"author":"Ivan"})
#
#pprint(result)

#result = list(persons.find({"autor": "Ivan"}))
#pprint(result)
#for doc in persons.find({"autor": "Ivan"}):
#    pprint(doc)

#for doc in persons.find({"autor": "Ivan", "age": 29}):
#    pprint(doc)

#for doc in persons.find({"$or":
#                             [{"autor":"Ivan"}, {"age":22}]
#                         }):
#    pprint(doc)

#for doc in persons.find({'age': {"$gte": 30}}):
#    pprint(doc)

#for doc in persons.find({"$or":
#                             [{'age': {"$lte": 25}}, {'age': {"$gte": 40}}]
#                         }):
#    pprint(doc)

#for doc in persons.find({'age': {"$gte": 25}, 'age': {"$lte": 40}}):
#    pprint(doc)

#for doc in persons.find({'age': {"$in": [22, 35]}}):
#    pprint(doc)

new_data = {
    "autor": "Andrey",
    "age": 28,
    "text": "is hot!",
    "date": "11.09.1991"}

#persons.update_one({"autor": "Ivan"}, {"$set": new_data})

#persons.replace_one({"autor": "Ivan"}, new_data)

persons.delete_one({"autor": "Ivan"})

#persons.delete_many({})

for doc in persons.find({}):
    pprint(doc)