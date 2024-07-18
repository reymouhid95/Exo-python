from abc import ABC, abstractmethod
import math


class Forme(ABC):
    @abstractmethod
    def calculerAire(self):
        pass

    def afficherType(self):
        print(f"Cette forme est un {self.__class__.__name__}")


class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculerAire(self):
        return math.pi * self.rayon ** 2


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculerAire(self):
        return self.longueur * self.largeur


# Utilisation du polymorphisme
formes = [Cercle(5), Rectangle(4, 6)]

for forme in formes:
    forme.afficherType()
    print(f"L'aire est : {forme.calculerAire()}")
    print()