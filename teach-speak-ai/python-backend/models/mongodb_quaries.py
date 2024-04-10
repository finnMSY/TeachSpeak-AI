from pymongo import MongoClient
from bson.objectid import ObjectId
from models.account import account
from models.hassaid import hassaid
from models.keyword import keyword
from models.school import school
from models.teacher import teacher

class mongodb_queries:
    def __init__(self, database):
        self.__db = database
        
    def get_all_from_accounts(self):
        return self.__db.Account.find()
    
    def get_all_from_hassaid(self):
        return self.__db.HasSaid.find()
    
    def get_all_from_keyword(self):
        return self.__db.Keyword.find()
    
    def get_all_from_school(self):
        return self.__db.School.find()
    
    def get_all_from_teacher(self):
        return self.__db.Teacher.find()