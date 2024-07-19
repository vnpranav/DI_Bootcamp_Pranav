import random

class Gene:
   def __init__(self):
      self.value = random.randint(0, 1)

   def flip(self):
      self.value = 1 - self.value

class Chromosome:
   def __init__(self, genes=[Gene()]*10):
      self.genes = genes

   def mutate(self):
      for gene in self.genes:
         if random.randint(0,1) == 1:
            gene.flip()

class DNA:
   def __init__(self, chromosomes=[Chromosome() ]* 10):
      self.chromosomes = chromosomes

   def mutate(self):
      for chromosome in self.chromosomes:
         chromosome.mutate()

class Organism:
   def __init__(self,environment ,dna=DNA()):
      self.dna = dna
      self.environment = environment

   def mutate(self):
      if random.randint(0,1) == self.environment:
         self.dna.mutate()

organism1 =  Organism(1)
organism2 =  Organism(0)
while True:
   organism1.mutate()
   organism2.mutate()

   count = 0
   for chromosome in organism1.dna.chromosomes:
      for gene in chromosome.genes:
         if gene.value == 1:
            count +=1
   if count == 10:
      break

   count = 0
   for chromosome in organism2.dna.chromosomes:
      for gene in chromosome.genes:
         if gene.value == 1:
            count +=1

   if count == 10:
      break