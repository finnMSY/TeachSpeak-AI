import account
import school

class teacher:
    def __init__(self, firstname, lastname, school, account, class_name):
        self.__id = None
        self.__firstname = firstname
        self.__lastname = lastname
        self.__school = school
        self.__account = account
        self.__class_name = class_name
    
    def get_id(self) -> int:
        return self.__id
    
    def get_firstname(self) -> str:
        return self.__firstname
    
    def get_lastname(self) -> str:
        return self.__lastname
    
    def get_school(self) -> school:
        return self.__school
    
    def get_account(self) -> account:
        return self.__account
    
    def get_class_name(self) -> str:
        return self.__class_name
    
    def get_json(self):
        pass
    