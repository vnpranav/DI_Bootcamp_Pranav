class Cat:
   def __init__(self, cat_name, cat_age):
      self.name = cat_name
      self.age = cat_age

   def __str__(self):
      return f"Cat {self.name} is {self.age} years old"

def find_oldest_cat(cats):
   cats.sort(key=lambda x: -x.age)
   return cats[0]

cat1 = Cat('meowth', 5)
cat2 = Cat('purrfect', 3)
cat3 = Cat('mew', 10)

cats = [cat1, cat2, cat3]
print(find_oldest_cat(cats))