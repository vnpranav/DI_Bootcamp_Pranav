class Family:
   def __init__(self, last_name, members=[]):
      self.last_name = last_name
      self.members = members

   def born(self, **kwargs):
      self.members.append(kwargs)
      print(f"congratulations on {kwargs['name']} being born")

   def is_18(self, name):
      for member in self.members:
         if member['name'] == name:
            if member['age'] >= 18:
               return True
            else:
               return False 
      return False
   
   def family_presentation(self):
        print(f"Family {self.last_name}:")
        for member in self.members:
            print(member.items())