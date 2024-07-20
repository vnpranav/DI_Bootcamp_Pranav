import string

def encrypt(text : str):
   # apply ceaser cypher
   # shift each letter by 3 positions
   # if the letter is 'z' then shift to 'c'
   cypher = ''
   for letter in text:
      if letter in string.ascii_lowercase:
         cypher +=  chr((ord(letter) - ord('a') + 3) % 26 + ord('a'))
      elif letter in string.ascii_uppercase:
         cypher +=  chr((ord(letter) - ord('A') + 3) % 26 + ord('A'))
      else:
         cypher += letter

   return cypher

def decrypt(cypher:str):
   decrypt = ''
   for letter in cypher:
      if letter in string.ascii_lowercase:
         decrypt += chr((ord(letter) - ord('a') - 3) % 26 + ord('a'))
      elif letter in string.ascii_uppercase:
         decrypt += chr((ord(letter) - ord('A') - 3) % 26 + ord('A'))
      else:
         decrypt += letter


   return decrypt

print(decrypt(encrypt("helLo")))
