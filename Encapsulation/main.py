class Personne:
    """
    Classe représentant une personne avec des attributs nom, âge et ville.
    """

    def __init__(self, nom, age, ville):
        """
        Constructeur de la classe Personne.

        :param nom: Le nom de la personne
        :param age: L'âge de la personne
        :param ville: La ville de résidence de la personne
        """
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    # Getters
    def get_nom(self):
        """Retourne le nom de la personne."""
        return self.__nom

    def get_age(self):
        """Retourne l'âge de la personne."""
        return self.__age

    def get_ville(self):
        """Retourne la ville de résidence de la personne."""
        return self.__ville

    # Setters
    def set_nom(self, nouveau_nom):
        """
        Modifie le nom de la personne.

        :param nouveau_nom: Le nouveau nom à attribuer
        """
        self.__nom = nouveau_nom

    def set_age(self, nouvel_age):
        """
        Modifie l'âge de la personne si la valeur est valide.

        :param nouvel_age: Le nouvel âge à attribuer
        """
        if nouvel_age >= 0:
            self.__age = nouvel_age
        else:
            print("L'âge doit être un nombre positif.")

    def set_ville(self, nouvelle_ville):
        """
        Modifie la ville de résidence de la personne.

        :param nouvelle_ville: La nouvelle ville à attribuer
        """
        self.__ville = nouvelle_ville