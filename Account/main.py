class CompteBancaire:
    def __init__(self, solde_initial=0):
        self.solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            return f"Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€"
        else:
            return "Erreur : Le montant du dépôt doit être positif."

    def retirer(self, montant):
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                return f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€"
            else:
                return "Erreur : Solde insuffisant."
        else:
            return "Erreur : Le montant du retrait doit être positif."

    def consulter_solde(self):
        return f"Solde actuel : {self.solde}€"

# Test des méthodes
compte = CompteBancaire(5000000000)  # Création d'un compte avec un solde initial de 1000€

print(compte.consulter_solde())
print(compte.deposer(500))
print(compte.retirer(200))
print(compte.consulter_solde())
print(compte.retirer(2000))  # Tentative de retrait d'un montant supérieur au solde
print(compte.deposer(-100))  # Tentative de dépôt d'un montant négatif