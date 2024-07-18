class MathUtil:
    @staticmethod
    def calculerMoyenne(nombres):
        if not nombres:
            return None
        return sum(nombres) / len(nombres)

# Exemple d'utilisation
nombres = [1, 2, 3, 4, 5]
moyenne = MathUtil.calculerMoyenne(nombres)
print(f"La moyenne est : {moyenne}")

# Pour un tableau vide
nombres_vides = []
moyenne_vide = MathUtil.calculerMoyenne(nombres_vides)
print(f"La moyenne d'un tableau vide est : {moyenne_vide}")