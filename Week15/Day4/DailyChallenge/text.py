import string
from collections import Counter

#  ---- part 1 ----
# class Text:
#     def __init__(self, txt_file):
#         self.text =  txt_file

#     def frequency(self, word_to_search):
#         words = self.text.split(" ")
#         count = 0

#         for w in words:
#             if w == word_to_search:
#                 count += 1
            
#         if count == 0:
#             return None
#         else:
#             return count
        
#     def most_common(self):
#         translator = str.maketrans("", "", string.punctuation)
#         words = self.text.translate(translator)
#         word_list = words.split()
         
#         frequencies = Counter(word_list)
#         return frequencies.most_common(1)
    
#     def sift(self):
#         translator = str.maketrans("", "", string.punctuation)
#         words = self.text.translate(translator)
#         word_list =  Counter(words.split())
        
#         keys = word_list.keys()
#         key_list = [key for key in keys]
#         return key_list
        
# sample = Text('a a a a a a b b b b b b b b  . . .. . .. . . . . . . . .  .. . . .. . . . . . . . x x x x x')
# print(sample.most_common())
# print(sample.sift())

class Text:
    def __init__(self, text_file):
        with open(text_file, 'r') as file:
            lines = file.readlines()
            
