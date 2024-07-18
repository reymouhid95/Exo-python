class Article:
    def __init__(self, nom, prix=0.0, quantite=0, reference=None, description=None):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        self.reference = reference
        self.description = description

    @classmethod
    def avec_nom(cls, nom):
        return cls(nom)

    @classmethod
    def avec_nom_et_prix(cls, nom, prix):
        return cls(nom, prix)

    @classmethod
    def avec_nom_prix_quantite(cls, nom, prix, quantite):
        return cls(nom, prix, quantite)

    @classmethod
    def avec_tous_les_details(cls, nom, prix, quantite, reference, description):
        return cls(nom, prix, quantite, reference, description)

    def __str__(self):
        return f"Article: {self.nom}, Prix: {self.prix}€, Quantité: {self.quantite}, Référence: {self.reference}, Description: {self.description}"