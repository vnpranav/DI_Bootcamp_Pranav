class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack

    def basic_attack(self, enemy):
        enemy.life -= self.attack
        if enemy.life <= 0:
            enemy.life = 0

class Druid(Character):
    def meditate(self):
        if self.attack > 0:
            self.attack -= 2
            self.life += 2
        
        if self.attack <= 0:
            self.attack = 0
        
    def animal_help(self):
        self.attack += 5

    def fight(self, enemy):
        enemy.life -= (0.75 * self.life + 0.75 * self.attack)
        if enemy.life <= 0:
            enemy.life = 0

class Warrior(Character):
    def brawl(self, enemy):
        enemy.life -= 2* self.attack
        if enemy.life <= 0:
            enemy.life = 0

        self.life += 0.5 * self.attack
    
    def train(self):
        self.attack += 2
        self.life +=2

    def roar(self, enemy):
        enemy.attack -= 3

        if enemy.attack <= 0:
            enemy.attack = 0

class Mage(Character):
    def curse(self, enemy):
        enemy.attack -= 2
        if enemy.attack <= 0:
            enemy.attack = 0

    def summon(self):
        self.attack += 3
    
    def cast_spell(self, enemy):
        enemy.life -= self.attack // self.life
        