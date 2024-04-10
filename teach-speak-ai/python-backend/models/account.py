class account:
    def __init__(self, username, password, account_type):
        self.__id = None
        self.__username = username
        self.__password = password
        self.__account_type = account_type
            
    def get_id(self) -> int:
        return self.__id
            
    def set_id(self, id):
        self.__id = id

    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_account_type(self):
        return self.__account_type
        
    def get_json(self):
        account_json = {"id": self.get_id(), "username": self.get_username(), "password": self.get_password(), "account_type": self.get_account_type}
        return account_json