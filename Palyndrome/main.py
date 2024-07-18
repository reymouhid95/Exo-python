def estPalindrome(mot):
    # Convertir le mot en minuscules et supprimer les espaces
    mot = mot.lower().replace(" ", "")
    # Comparer le mot avec son inverse
    return mot == mot[::-1]


def verifierPalindrome():
    # Demander à l'utilisateur de saisir un mot
    mot = input("Entrez un mot : ")

    # Vérifier si c'est un palindrome
    if estPalindrome(mot):
        print(f"'{mot}' est un palindrome.")
    else:
        print(f"'{mot}' n'est pas un palindrome.")


# Appeler la fonction pour tester
verifierPalindrome()