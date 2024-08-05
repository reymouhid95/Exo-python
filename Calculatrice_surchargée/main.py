from numbers import Number

class Calculatrice:
    @staticmethod
    def addition(*args):
        return sum(args)

    @staticmethod
    def soustraction(*args):
        if len(args) < 2:
            raise ValueError("La soustraction nécessite au moins deux arguments")
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

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

        operations = {
            '+': (self.addition, 0),
            '-': (self.soustraction, 2),
            '*': (self.multiplication, 0),
            '/': (self.division, 2)
        }

        if op not in operations:
            raise ValueError("Opération non reconnue")

        func, min_args = operations[op]
        if len(args) < min_args:
            raise ValueError(f"L'opération {op} nécessite au moins {min_args} arguments")

        return func(*args)

def get_numbers(min_count):
    numbers = []
    i = 1
    while True:
        try:
            num = input(f"Entrez le nombre {i} (ou appuyez sur Entrée pour terminer): ")
            if num == "" and len(numbers) >= min_count:
                break
            numbers.append(float(num))
            i += 1
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    return numbers

def main():
    calc = Calculatrice()
    operations = {
        '1': ('+', "Addition", 0),
        '2': ('-', "Soustraction", 2),
        '3': ('*', "Multiplication", 0),
        '4': ('/', "Division", 2)
    }

    while True:
        print("\nChoisissez une opération:")
        for key, (_, name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Quitter")

        choix = input("Entrez votre choix (1-5): ")

        if choix == '5':
            print("Au revoir!")
            break

        if choix not in operations:
            print("Choix invalide. Veuillez réessayer.")
            continue

        op, name, min_args = operations[choix]
        print(f"Entrez au moins {min_args} nombres pour {name.lower()} (appuyez sur Entrée sans rien écrire pour terminer):")

        try:
            nombres = get_numbers(min_args)
            resultat = calc.operation(op, *nombres)
            print(f"Résultat: {resultat}")
        except (ValueError, TypeError) as e:
            print(f"Erreur: {e}")

if __name__ == "__main__":
    main()