import random

class QuantumParticle:
   def __init__(self, position, momentum):
      choices = [1/2, -1/2,0]
      self.x = position
      self.p = momentum
      self.y = random.choice(choices[:2])

   def position(self):
      return random.randint(1, 10000)
   
   def momentum(self):
      return random.random()
   
   def spin(self):
      return random.choice([1/2, -1/2,0][:2])
   
   def disturbance(self):
      self.x = random.randint(1,10000)
      self.p = random.random()
      print("Quantum Interferences!!")

   def entangle(self, p2):
      self.x = -p2.x
      print("particle p1 is now entangled with particle p2")

      if self.x == -p2.x:
         print("spooky action at a distance")