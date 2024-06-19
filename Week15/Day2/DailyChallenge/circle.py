import math

class Circle():
    def __init__(self, choice, size):
        if choice == 'r':
            self.radius = size
            self.diameter = size * 2
        else:
            self.radius = size / 2
            self.diameter = size
        
    def area(self):
        return math.pi * (self.radius ** 2)
        
    def __repr__(self):
        return (f'Circle with Radius : {self.radius} & Diameter : {self.diameter}')
    
    def __add__(self, circle2):
        return Circle('r', self.radius + circle2.radius)
    
    def __gt__(self, circle2):
        if self.radius > circle2.radius:
            return True
        else:
            return False
        
    def __eq__(self, circle2):
        if self.radius == circle2.radius:
            return True
        else:
            return False


circ = Circle('r', 10)  
circ2 = Circle('r', 20)
circ3 = Circle('r', 5)
circles = [circ, circ2, circ3]        
circles.sort(key=lambda x: (x.radius))
print(circles)