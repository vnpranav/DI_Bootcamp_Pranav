import re

def find_numbers(expression):
   numbers = re.findall(r'\d' , expression)

   return ''.join(numbers)

print(find_numbers('k5k3q2g5z6x9bn'))