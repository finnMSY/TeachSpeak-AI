from pymongo import MongoClient
from bson.objectid import ObjectId
from models.keyword import keyword

client = MongoClient("mongodb+srv://Foxdapple:ymGbWgt6dFGtYOZJ@teachspeakcluster.4cgsjk6.mongodb.net/")

new_keyword = keyword("eggman")
new_keyword.set_id(1)
print(new_keyword.get_json())

# db = client.teachspeak

# for person in db.Teacher.find():
#     print(person) # gets the firstname from Teacher table