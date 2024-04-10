class keyword:
    def __init__(self, word):
        self.__id = None
        self.__word = word
            
    def get_id(self) -> int:
        return self.__id
        
    def set_id(self, id):
        self.__id = id

    def get_word(self):
        return self.__word
        
    def get_json(self):
        keyword = {"id": self.get_id(), "word": self.get_word()}
        return keyword