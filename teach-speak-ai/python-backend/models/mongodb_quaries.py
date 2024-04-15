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
        return self.__db.KeyWords.find()
    
    def get_all_from_school(self):
        return self.__db.School.find()
    
    def get_all_from_teacher(self):
        return self.__db.Teacher.find()
    
    def insert_one_into_accounts(self, account):
        self.__db.Account.insert_one(account.get_json())
    
    def insert_one_into_hassaid(self, hassaid):
        self.__db.HasSaid.insert_one(hassaid.get_json())
    
    def insert_one_into_keywords(self, keyword):
        self.__db.KeyWords.insert_one(keyword.get_json())
    
    def insert_one_into_schools(self, school):
        self.__db.School.insert_one(school.get_json())
    
    def insert_one_into_teachers(self, teacher):
        self.__db.Teacher.insert_one(teacher.get_json())
        
    def get_one_from_accounts(self, account):
        return self.__db.Account.find_one(account.get_json())
    
    def get_one_from_ahassaid(self, hassaid):
        return self.__db.HasSaid.find_one(hassaid.get_json())
    
    def get_one_from_keywords(self, keyword):
        return self.__db.KeyWords.find_one(keyword.get_json())
    
    def get_one_from_schools(self, school):
        return self.__db.School.find_one(school.get_json())
    
    def get_one_from_teachers(self, teacher):
        return self.__db.Teacher.find_one(teacher.get_json())