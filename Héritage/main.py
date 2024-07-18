class Animal:
    def __init__(self, nom):
        self.nom = nom

    def crier(self):
        pass


class Oiseau(Animal):
    def crier(self):
        print(f"{self.nom} fait Cui cui !")


class Chien(Animal):
    def crier(self):
        print(f"{self.nom} fait Woof woof !")


class Chat(Animal):
    def crier(self):
        print(f"{self.nom} fait Miaou !")


# Création d'objets
perroquet = Oiseau("Rio")
labrador = Chien("Max")
siamois = Chat("Whiskers")

# Utilisation du polymorphisme
animaux = [perroquet, labrador, siamois]

for animal in animaux:
    animal.crier()