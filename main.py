class Pet:
  def __init__(self, name, species, breed, age, weight):
    self.name = name
    self.species = species
    self.breed = breed
    self.age = age
    self.weight = weight

my_pet = Pet("Max","Dog","Boston Terrier",3,10)

print(my_pet.name)
print(my_pet.species)
print(my_pet.breed)
print(my_pet.weight)
print(my_pet.age)

