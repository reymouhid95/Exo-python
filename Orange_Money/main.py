import re
from typing import Optional, Tuple, List, Dict


class Transaction:
    def __init__(self, type: str, montant: float, details: str):
        self.type = type
        self.montant = montant
        self.details = details

    def __str__(self):
        return f"{self.type} : {self.montant:.2f} FCFA - {self.details}"


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
        return f"Votre solde est de {self.solde:.2f} FCFA"

    def effectuer_transaction(self, type: str, montant: float, details: str) -> str:
        if self.solde >= montant:
            self.solde -= montant
            self.transactions.append(Transaction(type, montant, details))
            return f"{type} de {montant:.2f} FCFA {details}. Nouveau solde : {self.solde:.2f} FCFA"
        return "Erreur : Solde insuffisant."

    def verifier_montant(self, montant: float, min_: float, max_: float) -> Optional[str]:
        if min_ <= montant <= max_:
            return None
        return f"Erreur : Le montant doit être entre {min_:.2f} et {max_:.2f} FCFA."

    def verifier_numero(self, numero: str) -> Tuple[bool, str]:
        pattern = r'^(77|78|76|70|75)\d{7}$'
        if re.match(pattern, numero):
            return True, ""
        return False, "Numéro de téléphone invalide. Il doit commencer par 77, 78, 76, 70 ou 75 et avoir 9 chiffres."

    def transfert_argent(self, montant: float, beneficiaire: str) -> str:
        erreur = self.verifier_montant(montant, self.TRANSFERT_MIN, self.TRANSFERT_MAX)
        if erreur:
            return erreur

        valide, message = self.verifier_numero(beneficiaire)
        if not valide:
            return message

        return self.effectuer_transaction("Transfert", montant, f"effectué à {beneficiaire}")

    def paiement_facture(self, montant: float, methode: str, details: str) -> str:
        if methode not in ["Liquide", "Chèque"]:
            return "Erreur : Méthode de paiement non reconnue."
        return self.effectuer_transaction(f"Paiement facture ({methode})", montant, details)

    def achat_credit(self, montant: float, numero: str) -> str:
        erreur = self.verifier_montant(montant, self.CREDIT_MIN, self.CREDIT_MAX)
        if erreur:
            return erreur

        valide, message = self.verifier_numero(numero)
        if not valide:
            return message

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
            while True:
                beneficiaire = input("Entrez le numéro du bénéficiaire : ")
                valide, message = self.verifier_numero(beneficiaire)
                if valide:
                    print(self.transfert_argent(montant, beneficiaire))
                    break
                print(message)

    def action_paiement_facture(self):
        while True:
            methode = input("Méthode de paiement (Liquide/Chèque) : ").capitalize()
            if methode in ["Liquide", "Chèque"]:
                break
            print("Erreur : Méthode de paiement non reconnue. Veuillez choisir Liquide ou Chèque.")

        montant = obtenir_montant("le paiement de la facture")
        if montant:
            details = input("Détails de la facture : ")
            print(self.paiement_facture(montant, methode, details))

    def action_achat_credit(self):
        montant = obtenir_montant("l'achat de crédit")
        if montant:
            while True:
                numero = input("Entrez le numéro de téléphone : ")
                valide, message = self.verifier_numero(numero)
                if valide:
                    print(self.achat_credit(montant, numero))
                    break
                print(message)


def obtenir_montant(operation: str) -> Optional[float]:
    while True:
        montant_str = input(f"Entrez le montant pour {operation} (ou 'q' pour annuler) : ")
        if montant_str.lower() == 'q':
            return None
        montant = OrangeMoney.convertir_montant(montant_str)
        if montant is not None:
            return montant
        print("Veuillez entrer un montant valide (en chiffres ou en lettres).")


if __name__ == "__main__":
    orange_money = OrangeMoney()
    orange_money.run()