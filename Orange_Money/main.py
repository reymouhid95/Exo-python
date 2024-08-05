import re
from typing import Optional, Tuple, List

class Transaction:
    def __init__(self, type: str, montant: float, details: str):
        self.type = type
        self.montant = montant
        self.details = details

    def __str__(self):
        return f"{self.type} : {self.montant} FCFA - {self.details}"

class OrangeMoney:
    TRANSFERT_MIN = 100
    TRANSFERT_MAX = 1000000
    CREDIT_MIN = 50
    CREDIT_MAX = 100000

    def __init__(self, solde_initial: float = 1000000):
        self.solde = solde_initial
        self.transactions: List[Transaction] = []

    def afficher_menu(self):
        menu_items = [
            "Solde de mon compte",
            "Transfert d'argent",
            "Paiement de facture",
            "Achats de crédit",
            "Consulter l'historique des transactions",
            "Quitter"
        ]
        print("\nMenu Orange Money:")
        for i, item in enumerate(menu_items, 1):
            print(f"{i}. {item}")

    def solde_compte(self) -> str:
        return f"Votre solde est de {self.solde} FCFA"

    def effectuer_transaction(self, type: str, montant: float, details: str) -> str:
        if self.solde >= montant:
            self.solde -= montant
            self.transactions.append(Transaction(type, montant, details))
            return f"{type} de {montant} FCFA {details}. Nouveau solde : {self.solde} FCFA"
        return "Erreur : Solde insuffisant."

    def verifier_montant(self, montant: float, min_: float, max_: float) -> Optional[str]:
        if min_ <= montant <= max_:
            return None
        return f"Erreur : Le montant doit être entre {min_} et {max_} FCFA."

    def transfert_argent(self, montant: float, beneficiaire: str) -> str:
        erreur = self.verifier_montant(montant, self.TRANSFERT_MIN, self.TRANSFERT_MAX)
        if erreur:
            return erreur
        return self.effectuer_transaction("Transfert", montant, f"effectué à {beneficiaire}")

    def paiement_facture(self, montant: float, methode: str, details: str) -> str:
        if methode not in ["Liquide", "Chèque"]:
            return "Erreur : Méthode de paiement non reconnue."
        return self.effectuer_transaction(f"Paiement facture ({methode})", montant, details)

    def achat_credit(self, montant: float, numero: str) -> str:
        erreur = self.verifier_montant(montant, self.CREDIT_MIN, self.CREDIT_MAX)
        if erreur:
            return erreur
        return self.effectuer_transaction("Achat crédit", montant, f"pour le numéro {numero}")

    def consulter_transactions(self) -> str:
        return "\n".join(map(str, self.transactions)) if self.transactions else "Aucune transaction enregistrée."

    @staticmethod
    def convertir_montant(montant_str: str) -> Optional[float]:
        nombres: Dict[str, int] = {
            'zéro': 0, 'un': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'cinq': 5, 'six': 6, 'sept': 7, 'huit': 8,
            'neuf': 9, 'dix': 10, 'onze': 11, 'douze': 12, 'treize': 13, 'quatorze': 14, 'quinze': 15, 'seize': 16,
            'vingt': 20, 'trente': 30, 'quarante': 40, 'cinquante': 50, 'soixante': 60, 'quatre vingts': 80,
            'quatre vingt': 80, 'cent': 100, 'mille': 1000, 'million': 1000000, 'milliard': 1000000000
        }

        def traiter_mot(mot: str) -> int:
            return nombres.get(mot, 0)

        def calculer_valeur(mots: List[str]) -> int:
            total, sous_total = 0, 0
            for mot in mots:
                valeur = traiter_mot(mot)
                if valeur in [100, 1000, 1000000, 1000000000]:
                    sous_total = max(1, sous_total) * valeur
                    if valeur >= 1000:
                        total += sous_total
                        sous_total = 0
                else:
                    sous_total += valeur
            return total + sous_total

        montant_str = montant_str.lower().replace(',', '.').replace('-', ' ')

        # Tentative de conversion directe en nombre
        try:
            return float(montant_str)
        except ValueError:
            pass

        # Traitement comme nombre écrit en toutes lettres
        mots = montant_str.split()
        if len(mots) == 1 and mots[0] in nombres:
            return float(nombres[mots[0]])

        valeur = calculer_valeur(mots)
        return float(valeur) if valeur else None

    def run(self):
        actions = {
            '1': lambda: print(self.solde_compte()),
            '2': self.action_transfert,
            '3': self.action_paiement_facture,
            '4': self.action_achat_credit,
            '5': lambda: print(self.consulter_transactions()),
            '6': lambda: print("Merci d'avoir utilisé Orange Money. Au revoir!")
        }

        while True:
            self.afficher_menu()
            choix = input("Votre choix : ")
            action = actions.get(choix)
            if action:
                if choix == '6':
                    action()
                    break
                action()
            else:
                print("Choix invalide. Veuillez réessayer.")

    def action_transfert(self):
        montant = obtenir_montant("le transfert")
        if montant:
            beneficiaire = input("Entrez le numéro du bénéficiaire : ")
            print(self.transfert_argent(montant, beneficiaire))

    def action_paiement_facture(self):
        methode = input("Méthode de paiement (Liquide/Chèque) : ")
        montant_str = input("Entrez le montant (en chiffres ou en lettres) : ")
        montant = self.convertir_montant(montant_str)
        if montant:
            details = input("Détails de la facture : ")
            print(self.paiement_facture(montant, methode, details))
        else:
            print("Erreur : Montant invalide.")

    def action_achat_credit(self):
        montant = obtenir_montant("l'achat de crédit")
        if montant:
            numero = input("Entrez le numéro de téléphone : ")
            print(self.achat_credit(montant, numero))

def obtenir_montant(operation: str) -> Optional[float]:
    while True:
        montant = input(f"Entrez le montant pour {operation} (ou 'q' pour annuler) : ")
        if montant.lower() == 'q':
            return None
        try:
            return float(montant)
        except ValueError:
            print("Veuillez entrer un nombre valide.")

if __name__ == "__main__":
    orange_money = OrangeMoney()
    orange_money.run()