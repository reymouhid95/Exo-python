import copy

class Article:
    def __init__(self, nom, prix=0.0, quantite=0, reference=None, description=None):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        self.reference = reference
        self.description = description

    def __str__(self):
        return f"Article: {self.nom}, Prix: {self.prix}€, Quantité: {self.quantite}, Référence: {self.reference}, Description: {self.description}"

    def modifier(self, attribut, nouvelle_valeur):
        if hasattr(self, attribut):
            ancienne_valeur = getattr(self, attribut)
            setattr(self, attribut, nouvelle_valeur)
            print(f"{attribut.capitalize()} modifié avec succès.")
            return ancienne_valeur
        else:
            print(f"L'attribut {attribut} n'existe pas.")
            return None


class GestionnaireArticles:
    def __init__(self):
        self.articles = []
        self.historique = []

    def creer_article(self):
        nom = input("Nom de l'article : ")
        prix = self.saisir_nombre_float("Prix de l'article : ")
        quantite = self.saisir_nombre_int("Quantité de l'article : ")
        reference = input("Référence de l'article (appuyez sur Entrée si non applicable) : ") or None
        description = input("Description de l'article (appuyez sur Entrée si non applicable) : ") or None

        article = Article(nom, prix, quantite, reference, description)
        self.articles.append(article)
        self.historique.append(("creer", len(self.articles) - 1, None))
        print("Article créé avec succès.")

    def afficher_articles(self):
        if not self.articles:
            print("Aucun article à afficher.")
            return
        for i, article in enumerate(self.articles, 1):
            print(f"{i}. {article}")

    def modifier_article(self):
        if not self.articles:
            print("Aucun article à modifier.")
            return

        self.afficher_articles()
        index = self.saisir_nombre_int("Entrez le numéro de l'article à modifier : ") - 1

        if 0 <= index < len(self.articles):
            article = self.articles[index]
            attribut = self.choisir_attribut()
            if attribut:
                nouvelle_valeur = input(f"Nouvelle valeur pour {attribut} : ")
                if attribut in ['prix', 'quantite']:
                    nouvelle_valeur = float(nouvelle_valeur) if attribut == 'prix' else int(nouvelle_valeur)
                ancienne_valeur = article.modifier(attribut, nouvelle_valeur)
                self.historique.append(("modifier", index, (attribut, ancienne_valeur)))
        else:
            print("Numéro d'article invalide.")

    def annuler(self):
        if not self.historique:
            print("Aucune action à annuler.")
            return

        derniere_action = self.historique.pop()
        type_action, index, details = derniere_action

        if type_action == "creer":
            self.articles.pop()
            print("Création d'article annulée.")
        elif type_action == "modifier":
            attribut, ancienne_valeur = details
            self.articles[index].modifier(attribut, ancienne_valeur)
            print(f"Modification de l'attribut {attribut} annulée.")

    @staticmethod
    def saisir_nombre_float(message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Veuillez entrer un nombre valide.")

    @staticmethod
    def saisir_nombre_int(message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

    @staticmethod
    def choisir_attribut():
        attributs = ['nom', 'prix', 'quantite', 'reference', 'description']
        print("Quel attribut voulez-vous modifier ?")
        for i, attr in enumerate(attributs, 1):
            print(f"{i}. {attr.capitalize()}")
        choix = GestionnaireArticles.saisir_nombre_int("Entrez le numéro de votre choix : ")
        return attributs[choix - 1] if 1 <= choix <= len(attributs) else None


def afficher_menu():
    print("\nQue voulez-vous faire ?")
    print("1. Créer un nouvel article")
    print("2. Afficher tous les articles")
    print("3. Modifier un article")
    print("4. Annuler la dernière action")
    print("5. Quitter")


def main():
    gestionnaire = GestionnaireArticles()

    while True:
        afficher_menu()
        choix = input("Entrez le numéro de votre choix : ")

        if choix == "1":
            gestionnaire.creer_article()
        elif choix == "2":
            gestionnaire.afficher_articles()
        elif choix == "3":
            gestionnaire.modifier_article()
        elif choix == "4":
            gestionnaire.annuler()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()