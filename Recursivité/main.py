def calculerFactorielle(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat

# Exemple d'utilisation
nombre = 5
resultat = calculerFactorielle(nombre)
print(f"La factorielle de {nombre} est : {resultat}")
