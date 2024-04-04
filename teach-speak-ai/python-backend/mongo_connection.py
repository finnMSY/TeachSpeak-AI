from pymongo import MongoClient

client = MongoClient("mongodb+srv://Foxdapple:ymGbWgt6dFGtYOZJ@teachspeakcluster.4cgsjk6.mongodb.net/")

db = client.teachspeak

for person in db.Teacher.find():
    print(person["firstname"]) # gets the firstname from Teacher table