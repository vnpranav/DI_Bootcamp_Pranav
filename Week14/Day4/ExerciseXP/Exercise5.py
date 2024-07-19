from Exercise4 import Family

class TheIncredibles(Family):
   def __init__(self, members=[]):
      Family.__init__(self, members)

   def use_power(self, name):
      try:
         if self.is_18(name) == True:
            for member in self.members:
               if member.name == name:
                  print(f"member uses {member['power']}")
         else:
            raise Exception("under 18")
      except Exception as e:
         print(e)
      
   def incredible_presentation(self):
      print("here is our powerful family")
      print(self.last_name)
      Family.family_presentation(self)
