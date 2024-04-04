class school:
    def __init__(self, name, location):
        self.__id = None
        self.__name = name
        self.__location = location
    
    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location
        
    def get_json(self):
        pass