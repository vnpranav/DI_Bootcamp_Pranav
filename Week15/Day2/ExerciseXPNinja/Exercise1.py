class Temperature:
   def __init__(self, temperature):
      self.temperature = temperature

class Kelvin(Temperature):
   unit = 'K'

   def to_Celcius(self):
      return self.temperature - 273.15
   
   def to_Farenheit(self):
      return (self.temperature - 273.15) * 1.8 + 32
   
class Celcius(Temperature):
   unit = 'C'

   def to_Kelvin(self):
      return self.temperature + 273.15
   
   def to_Farenheit(self):
      return (self.temperature + 273.15) * 1.8 - 459.
   
class Farenheit(Temperature):
   unit = 'F'

   def to_Celcius(self):
      return (self.temperature + 459.67) / 1.8 - 273.15

   def to_Kelvin(self):
      return (self.temperature + 459.67) / 1.8