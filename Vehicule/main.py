from abc import ABC, abstractmethod

class Vehicule(ABC):
    @abstractmethod
    def deplacer(self):
        pass

class Voiture(Vehicule):
    def deplacer(self):
        print("La voiture roule sur la route.")

class Avion(Vehicule):
    def deplacer(self):
        print("L'avion vole dans les airs.")

class Bateau(Vehicule):
    def deplacer(self):
        print("Le bateau navigue sur l'eau.")

# Test des classes
voiture = Voiture()
avion = Avion()
bateau = Bateau()

voiture.deplacer()
avion.deplacer()
bateau.deplacer()