import re


class CompteBancaire:
    # Constantes pour les limites de retrait et de chèque
    RETRAIT_MIN = 50
    RETRAIT_MAX = 2000
    CHEQUE_MIN = 100
    CHEQUE_MAX = 5000

    def __init__(self, solde_initial=0):
        """Initialise un compte bancaire avec un solde initial."""
        self.solde = solde_initial
        self.cheques_emis = []

    def deposer(self, montant):
        """Dépose un montant sur le compte."""
        if montant > 0:
            self.solde += montant
            return f"Dépôt de {montant}€ effectué. Nouveau solde : {self.solde}€"
        else:
            return "Erreur : Le montant du dépôt doit être positif."

    def retirer(self, montant):
        """Retire un montant du compte si les conditions sont remplies."""
        if self.RETRAIT_MIN <= montant <= self.RETRAIT_MAX:
            if self.solde >= montant:
                self.solde -= montant
                return f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€"
            else:
                return "Erreur : Solde insuffisant."
        else:
            return f"Erreur : Le montant du retrait doit être entre {self.RETRAIT_MIN}€ et {self.RETRAIT_MAX}€."

    def consulter_solde(self):
        """Renvoie le solde actuel du compte."""
        return f"Solde actuel : {self.solde}€"

    def emettre_cheque(self, montant_str, beneficiaire):
        """Émet un chèque si les conditions sont remplies."""
        montant = self.convertir_montant(montant_str)
        if montant is None:
            return "Erreur : Montant invalide."

        if self.CHEQUE_MIN <= montant <= self.CHEQUE_MAX:
            if self.solde >= montant:
                self.solde -= montant
                self.cheques_emis.append((montant_str, beneficiaire))
                return f"Chèque de {montant_str}€ émis à {beneficiaire}. Nouveau solde : {self.solde}€"
            else:
                return "Erreur : Solde insuffisant pour émettre ce chèque."
        else:
            return f"Erreur : Le montant du chèque doit être entre {self.CHEQUE_MIN}€ et {self.CHEQUE_MAX}€."

    def consulter_cheques(self):
        """Renvoie la liste des chèques émis."""
        if not self.cheques_emis:
            return "Aucun chèque émis."
        return "\n".join([f"Chèque de {montant}€ à {beneficiaire}" for montant, beneficiaire in self.cheques_emis])

    @staticmethod
    def convertir_montant(montant_str):
        """Convertit un montant en chaîne (chiffres ou lettres) en nombre."""
        montant_str = montant_str.lower().replace(',', '.')
        nombres = {
            'zéro': 0, 'un': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'cinq': 5, 'six': 6, 'sept': 7, 'huit': 8,
            'neuf': 9,
            'dix': 10, 'onze': 11, 'douze': 12, 'treize': 13, 'quatorze': 14, 'quinze': 15, 'seize': 16,
            'vingt': 20, 'trente': 30, 'quarante': 40, 'cinquante': 50, 'soixante': 60, 'quatre-vingt': 80,
            'cent': 100, 'mille': 1000, 'million': 1000000, 'milliard': 1000000000
        }

        if montant_str in nombres:
            return nombres[montant_str]

        try:
            return float(montant_str)
        except ValueError:
            # Traitement des montants écrits en toutes lettres
            mots = re.findall(r'\w+', montant_str)
            total = 0
            sous_total = 0
            for mot in mots:
                if mot in nombres:
                    if nombres[mot] == 100:
                        sous_total = sous_total * 100 if sous_total else 100
                    elif nombres[mot] in [1000, 1000000, 1000000000]:
                        sous_total = sous_total * nombres[mot] if sous_total else nombres[mot]
                        total += sous_total
                        sous_total = 0
                    else:
                        sous_total += nombres[mot]
            total += sous_total
            return total if total else None


def obtenir_montant(operation):
    """Demande et renvoie un montant pour une opération donnée."""
    while True:
        montant = input(f"Entrez le montant pour {operation} (ou 'q' pour annuler) : ")
        if montant.lower() == 'q':
            return None
        if operation == "le chèque":
            return montant  # Retourne le montant comme une chaîne pour les chèques
        try:
            return float(montant)
        except ValueError:
            print("Veuillez entrer un nombre valide.")


def main():
    """Fonction principale gérant l'interface utilisateur."""
    compte = CompteBancaire(1000)  # Création d'un compte avec un solde initial de 1000€

    while True:
        print("\nQue voulez-vous faire ?")
        print("1. Consulter le solde")
        print("2. Faire un dépôt")
        print("3. Faire un retrait")
        print("4. Émettre un chèque")
        print("5. Consulter les chèques émis")
        print("6. Quitter")

        choix = input("Entrez votre choix (1-6) : ")

        if choix == '1':
            print(compte.consulter_solde())
        elif choix == '2':
            montant = obtenir_montant("le dépôt")
            if montant is not None:
                print(compte.deposer(montant))
        elif choix == '3':
            print(f"Rappel : Le retrait doit être entre {CompteBancaire.RETRAIT_MIN}€ et {CompteBancaire.RETRAIT_MAX}€")
            montant = obtenir_montant("le retrait")
            if montant is not None:
                print(compte.retirer(montant))
        elif choix == '4':
            print(
                f"Rappel : Le montant du chèque doit être entre {CompteBancaire.CHEQUE_MIN}€ et {CompteBancaire.CHEQUE_MAX}€")
            montant = obtenir_montant("le chèque")
            if montant is not None:
                beneficiaire = input("Entrez le nom du bénéficiaire : ")
                print(compte.emettre_cheque(montant, beneficiaire))
        elif choix == '5':
            print(compte.consulter_cheques())
        elif choix == '6':
            print("Merci d'avoir utilisé notre service bancaire. Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()