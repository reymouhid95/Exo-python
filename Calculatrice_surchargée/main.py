from numbers import Number


class Calculatrice:
    @staticmethod
    def addition(*args):
        return sum(args)

    @staticmethod
    def soustraction(a, b):
        return a - b

    @staticmethod
    def multiplication(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def division(a, b):
        if isinstance(b, (int, float)) and b == 0:
            raise ValueError("Division par zéro impossible")
        return a / b

    def operation(self, op, *args):
        if not all(isinstance(arg, Number) for arg in args):
            raise TypeError("Tous les arguments doivent être des nombres")

        if op == '+':
            return self.addition(*args)
        elif op == '-':
            if len(args) != 2:
                raise ValueError("La soustraction nécessite exactement deux arguments")
            return self.soustraction(*args)
        elif op == '*':
            return self.multiplication(*args)
        elif op == '/':
            if len(args) != 2:
                raise ValueError("La division nécessite exactement deux arguments")
            return self.division(*args)
        else:
            raise ValueError("Opération non reconnue")


def main():
    calc = Calculatrice()

    while True:
        print("\nChoisissez une opération:")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")

        choix = input("Entrez votre choix (1-5): ")

        if choix == '5':
            print("Au revoir!")
            break

        if choix not in ['1', '2', '3', '4']:
            print("Choix invalide. Veuillez réessayer.")
            continue

        try:
            if choix in ['1', '3']:  # Addition et multiplication peuvent avoir plusieurs arguments
                nombres = input("Entrez les nombres séparés par des espaces: ").split()
                nombres = [float(n) for n in nombres]
            else:  # Soustraction et division n'ont que deux arguments
                a = float(input("Entrez le premier nombre: "))
                b = float(input("Entrez le deuxième nombre: "))
                nombres = [a, b]

            if choix == '1':
                resultat = calc.operation('+', *nombres)
            elif choix == '2':
                resultat = calc.operation('-', *nombres)
            elif choix == '3':
                resultat = calc.operation('*', *nombres)
            elif choix == '4':
                resultat = calc.operation('/', *nombres)

            print(f"Résultat: {resultat}")

        except ValueError as e:
            print(f"Erreur: {e}")
        except TypeError as e:
            print(f"Erreur: {e}")


if __name__ == "__main__":
    main()