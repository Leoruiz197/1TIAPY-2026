from Cachorro import Cachorro

from Gato import Gato

cachorro1 = Cachorro("Rex", "Cachorro", 20, "Labrador")
gato1 = Gato("Mia", "Gato", 5, "Curta")

print(cachorro1.name)
print(cachorro1.species)
print(cachorro1.weight)
print(cachorro1.raca)
print(cachorro1.fazerSom())
print(cachorro1.correr())

print(gato1.name)
print(gato1.species)   
print(gato1.weight)
print(gato1.pelagem)
print(gato1.fazerSom())
print(gato1.comer())