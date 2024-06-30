def check_parentheses(expression: str):
   starting = ['(', '[','{' ]
   ending = [')', ']', '}']
   matches = list(zip(starting , ending)) 

   parentheses = []

   for char in expression:
      if char in starting:
         parentheses.append(char)
      elif char in ending:
         combined = (parentheses[len(parentheses) - 1], char)
         if combined in matches:
            parentheses.pop()

   if len(parentheses) == 0:
      return True
   else:
      return False
   
print(check_parentheses(str("((1 + 2)")))
