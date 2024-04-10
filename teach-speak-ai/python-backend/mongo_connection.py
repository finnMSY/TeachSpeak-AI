from pymongo import MongoClient
from bson.objectid import ObjectId
from models.keyword import keyword
from models.mongodb_quaries import mongodb_queries

client = MongoClient("mongodb+srv://Foxdapple:ymGbWgt6dFGtYOZJ@teachspeakcluster.4cgsjk6.mongodb.net/")

new_keyword = keyword("eggman")

db = client.teachspeak

query_repository = mongodb_queries(db)

for person in query_repository.get_all_from_teacher():
    print(person) # gets the firstname from Teacher table

# for person in db.Teacher.find():
#     print(person) # gets the firstname from Teacher table