class BankAccount:         
   def __init__(self, balance, username, password, authenticated=False):
      self.balance = balance
      self.username = username
      self.password = password
      self.authenticated = authenticated

   def deposit(self,amount):
      try:
         if amount > 0:
            self.balance += amount
         else:
            raise ValueError("Invalid amount")
      except Exception as e:
         print(e)
      
   def withdraw(self, amount):
      try:
         if amount > 0 and self.authenticated == True:
            self.balance -= amount
         else:
            raise ValueError("Invalid amount")
      except Exception as e:
         print(e)
   
   def authenticate(self,username, password):
      if self.username == username and self.password == password:
         self.authenticated = True
         return True
      else:
         return False

class MinimumBalanceAccount(BankAccount):
   def __init__(self, balance, username, password, authenticated=False ,min_balance=0):
      BankAccount.__init__(self, balance,username, password, authenticated)
      self.minimum_balance = min_balance

   def withdraw(self, amount):
      try:
         if (self.balance - amount < self.minimum_balance or amount < 0 or self.minimum_balance == self.balance) and self.authenticated == True:
            raise ValueError("Insufficient balance")
         else:
            self.balance -= amount
      except Exception as e:
         print(e)
   

class ATM:
   def __init__(self, account_list, try_limit):
      self.accounts_list = []
      for account in account_list:
         if isinstance(account, BankAccount) or isinstance(account, MinimumBalanceAccount):
            self.accounts_list.append(account)

      try:
         self.try_limit = int(try_limit)
         if try_limit < 0:
            raise ValueError("should be greater than 0")
      except Exception as e:
         print(e)
         self.try_limit = 2
   
      self.current_tries = 0

   def show_main_menu(self):
      while True:
         print("1. Login")
         print("2. Exit")

         choice = int(input("Choose option: "))

         if choice ==2:
            break
         elif choice == 1:
            account = self.log_in()
            if account is not None:
               self.show_account_menu(account)

   def log_in(self):
      username = input("Enter username: ")
      password = input("Enter password: ")
      for account in self.accounts_list:
         if account.authenticate(username, password):
            return account
      return None
   
   def show_account_menu(self, account):
         while True:
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Exit")
            choice = int(input("Choose option: "))
            if choice == 1:
               amt = input("Enter amount")
               account.withdraw(amt)
            elif choice == 2:
               amt = input("Enter amount")
               account.deposit(amt)
            elif choice == 3:
               break
            
