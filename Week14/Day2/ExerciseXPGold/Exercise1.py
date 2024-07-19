class Circle:
   def __init__(self, radius):
      self.radius = radius
   
   def area(self):
      return 3.14 * self.radius ** 2
   
   def perimeter(self):
      return 2 * 3.14 * self.radius
   
   def __repr__(self) -> str:
      return f"Circle with radius {self.radius}, perimeter {self.perimeter()} and area {self.area()}"