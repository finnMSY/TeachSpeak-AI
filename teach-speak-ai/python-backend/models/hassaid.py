import keyword
import teacher

class hassaid:
    def __init__(self, word, teacher):
        self.__id = None
        self.__word = word
        self.__teacher = teacher
            
    def get_id(self) -> int:
        return self.__id
            
    def set_id(self, id):
        self.__id = id

    def get_word(self):
        return self.__word
    
    def get_teacher(self):
        return self.__teacher
        
    def get_json(self):
        hassaid_json = {"id": self.get_id(), "word": self.get_word(), "teacher": self.get_teacher}
        return hassaid_json
