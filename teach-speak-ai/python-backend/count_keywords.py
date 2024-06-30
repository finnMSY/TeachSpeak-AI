from collections import defaultdict
import os

def get_keywords():
    keywords_const_path = os.path.abspath("keywords.txt")
    with open(keywords_const_path, 'r') as file:
        lines = file.readlines()    

    return [line.strip() for line in lines]
  
def count_keywords(text: str):
    keyword_counts = defaultdict(int)
    keywords = get_keywords()
    words = text.split(" ")
    words_to_remove = [",", ".", "?", "!"]
    for word in words:
        for word_to_remove in words_to_remove:
            word = word.lower().replace(word_to_remove, "")

        if word in keywords:
            keyword_counts[word] += 1
    return keyword_counts