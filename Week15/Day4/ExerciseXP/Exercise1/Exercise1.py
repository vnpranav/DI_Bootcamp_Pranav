import random

def get_words_from_file():
    try:
        with open('wordslist.txt') as file:
            words = file.readlines()

            return words
    except:
        return []
    
def get_random_sentence(length):
    sentence = ""
    words = get_words_from_file()

    for i in range(length):
        sentence += random.choice(words).replace("\n", " ")
    
    return sentence

print(get_random_sentence(5))


