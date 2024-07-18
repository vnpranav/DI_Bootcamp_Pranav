from menu_manager import MenuManager

def load_manager():
   return MenuManager()

def show_user_menu():
   while True:
      print("1. Add new item")
      print("2. Remove item")
      print("3. show menu")
      print("4. Exit")

      choice  =int(input("enter choice: "))
      manager = load_manager()

      if choice == 1:
         name = input("enter name: ")
         price = int(input("enter price: "))
         manager.add_item(name, price)
      elif choice == 2:
         name = input("enter name: ")
         if manager.remove_item(name):
            print("item removed")
         else: 
            print("item not found")
      elif choice == 3:
         print(manager.menu)
      elif choice == 4:
         manager.save_to_file()
         break

   
