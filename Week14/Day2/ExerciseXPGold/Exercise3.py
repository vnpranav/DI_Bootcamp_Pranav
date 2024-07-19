class MenuManager:
   def __init__(self):
      self.menu = []

   def add_menu_item(self, name, price, spice, gluten):
      new_item = {
         "name" : name,
         "price" : price,
         "spice" : spice,
         "gluten" : gluten
      }

      self.menu.append(new_item)

   def update_item(self, name, price, spice, gluten):
      found = False
      for item in self.menu:
         if item["name"] == name:
            item["price"] = price
            item["spice"] = spice
            item["gluten"] = gluten
            found = True
            break

         if not found:
            print("Item not found")

   def remove_item(self,name):
      found = False
      for item in self.menu:
         if item["name"] == name:
            self.menu.remove(item)
            found = True
            break
      
      if not found:
         print("item not found")
      else:
         for item in self.menu:
            print(f"{item['name']} : {item['price']}, {item['price']}, {item['gluten']}")
