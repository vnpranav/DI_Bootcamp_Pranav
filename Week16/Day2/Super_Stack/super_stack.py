class Superstack():
   def __init__(self):
      self.stack = []

   def push(self,v):
      self.stack.append(v)
   
   def pop(self):
      if len(self.stack) > 0:
         return self.stack.pop()
      else:
         return 'Empty'
   
   def inc(self, i, v):
      to_update = self.stack[:i]

      if i > len(to_update):
         print("stack too small")
      else:
         for item in to_update:
            item += v
      
      self.stack = to_update + self.stack[i:]
   
   def __str__(self):
      return f'{self.stack}'
   
stack = Superstack()
stack.push(4)
stack.push(5)
print(stack)
stack.inc(2,1)
print(stack)
print(stack.pop())
print(stack)
