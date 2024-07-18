import random
import string

def generate_pw(length):
   lower = string.ascii_lowercase
   upper = string.ascii_uppercase
   digits = string.digits
   symbols = string.punctuation

   password = []
   password.append(random.choice(lower))
   password.append(random.choice(upper))
   password.append(random.choice(digits))
   password.append(random.choice(symbols))

   for i in range(length - 4):
      password.append(random.choice(lower+upper+digits+symbols))

   random.shuffle(password)
   return ''.join((password))

while True:
   length = int(input('Enter desired password length: '))
   if length >= 6 and length <=30:
      break