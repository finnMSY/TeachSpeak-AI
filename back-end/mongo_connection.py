from pymongo import MongoClient
from bson.objectid import ObjectId
from models.account import account
from models.hassaid import hassaid
from models.keyword import keyword
from models.school import school
from models.teacher import teacher

from models.mongodb_quaries import mongodb_queries

'''
Could add ObjectID() into each model to store it in self.___id with _id being the ID in MongoDB
If this were to be done, self.__id would need to be changed into self.___id

Could also do it without ObjectID as MongoDB allows storing Json's within entries
    Discuss this with Finn and Oliver
'''


client = MongoClient("mongodb+srv://Foxdapple:ymGbWgt6dFGtYOZJ@teachspeakcluster.4cgsjk6.mongodb.net/")

new_keyword = keyword("testing")
new_school = school("Mahurangi College", "Warkworth")
new_account = account("Foxdapple", "testing", "normal")


db = client.teachspeak

query_repository = mongodb_queries(db)
# query_repository.insert_one_into_schools(new_school)
# query_repository.insert_one_into_accounts(new_account)

new_school = query_repository.get_one_from_schools(new_school)
new_account = query_repository.get_one_from_accounts(new_account)

new_teacher = teacher("Aaron", "Heald", ObjectId(new_school["_id"]), ObjectId(new_account["_id"]), "Science?")
query_repository.insert_one_into_teachers(new_teacher)

for person in query_repository.get_all_from_teacher():
    print(person) # gets the firstname from Teacher table
    
# query_repository.insert_one_into_keywords(new_keyword)
# print()

# for person in db.Teacher.find():
#     print(person) # gets the firstname from Teacher table