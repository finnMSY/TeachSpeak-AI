from pymongo import MongoClient
from bson.objectid import ObjectId
from models.account import account
from models.hassaid import hassaid
from models.keyword import keyword
from models.school import school
from models.teacher import teacher

from models.mongodb_quaries import mongodb_queries
# from transcribe_audio import transcribe_audio

'''
Could add ObjectID() into each model to store it in self.___id with _id being the ID in MongoDB
If this were to be done, self.__id would need to be changed into self.___id

Could also do it without ObjectID as MongoDB allows storing Json's within entries
    Discuss this with Finn and Oliver
'''
# Set's up db connection and the query model for querying the DB
client = MongoClient("mongodb+srv://Foxdapple:ymGbWgt6dFGtYOZJ@teachspeakcluster.4cgsjk6.mongodb.net/")
db = client.teachspeak
query_repository = mongodb_queries(db)


'''
Example connection used to run tests, can be removed whenever.
Probably needs simplification to get the objectID (might just generate them and get them that way)
    Can do this by just incrementing the id each time instead
'''
new_school = school("Mahurangi College", "Warkworth")
new_account = account("Foxdapple", "testing", "normal")
new_school = query_repository.get_one_from_schools(new_school)
new_account = query_repository.get_one_from_accounts(new_account)

new_teacher = teacher("Aaron", "Heald", ObjectId(new_school["_id"]), ObjectId(new_account["_id"]), "Science?")

def create_entry(teacher, frequency):
    teacher_id = query_repository.get_one_from_teachers(teacher)["_id"]
    entry = hassaid(frequency, ObjectId(teacher_id))
    query_repository.insert_one_into_hassaid(entry)
    return 

def get_keywords():
    keyword_json = query_repository.get_all_from_keyword()
    keywords = []
    for i in keyword_json:
        keywords.append(i["word"])
    return keywords

def count_frequency(audio_text): # Might note work, needs to be tested, currently cannot as speech_recognition not installing - Aaron
    frequency = {}               # This is currently written to work with a String input
    list_of_words = audio_text.split()
    keywords = get_keywords()
    for word in list_of_words:
        if word in keywords:
            if word not in frequency:
                frequency[word] = 1
            else:
                frequency[word] += 1
    return frequency

def run_word_check(text, teacher):
    frequency = count_frequency(text)
    create_entry(teacher, frequency)

run_word_check("Egg man test issue", new_teacher)



# new_keyword = keyword("testing")
# new_school = school("Mahurangi College", "Warkworth")
# new_account = account("Foxdapple", "testing", "normal")


# db = client.teachspeak

# query_repository = mongodb_queries(db)
# # query_repository.insert_one_into_schools(new_school)
# # query_repository.insert_one_into_accounts(new_account)

# new_school = query_repository.get_one_from_schools(new_school)
# new_account = query_repository.get_one_from_accounts(new_account)


# query_repository.insert_one_into_teachers(new_teacher)

# for person in query_repository.get_all_from_teacher():
#     print(person) # gets the firstname from Teacher table
    
# # query_repository.insert_one_into_keywords(new_keyword)
# # print()

# # for person in db.Teacher.find():
# #     print(person) # gets the firstname from Teacher table