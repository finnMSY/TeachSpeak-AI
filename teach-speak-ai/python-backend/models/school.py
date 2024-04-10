class school:
    def __init__(self, name, location):
        self.__id = None
        self.__name = name
        self.__location = location
            
    def get_id(self) -> int:
        return self.__id
            
    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name
    
    def get_location(self):
        return self.__location
        
    def get_json(self):
        school_json = {"name": self.get_name(), "location": self.get_location()}
        return school_json