import keyword
import teacher

class hassaid:
    def __init__(self, word, teacher):
        self.__word = word
        self.__teacher = teacher
    
    def get_word(self):
        return self.__word
    
    def get_teacher(self):
        return self.__teacher
        
    def get_json(self):
        pass