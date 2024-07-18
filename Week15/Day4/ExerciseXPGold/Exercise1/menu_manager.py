import json

class MenuManager:
   # get data from restaurant_menu.json
   def __init__(self):
      self.menu = self.read_menu()

   def read_menu(self):
      with open('./restaurant_menu.json', 'r') as f:
         menu_data = json.load(f)
      return menu_data['items']
   
   def add_item(self, name, price):
      self.menu[name] = price

   def remove_item(self,name):
      if name in self.menu.keys():
         del self.menu[name]
         return True
      else:
         return False
      
   def save_to_file(self):
      with open('./restaurant_menu.json', 'w') as f:
         json.dump(self.menu, f, indent=4)

manager = MenuManager()
print(manager.menu)