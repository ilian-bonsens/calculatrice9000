historique = ""

def calculatrice():
    global historique
    while True:
        try:
            num1 = float(input("Entrez un nombre valide : "))
            break
        except ValueError: 
            print("Erreur : entrez un caractère valide (nombre).")

    while True:
        try:
            operation = input("Type d'opération (+, -, *, /, **) : ")
            if operation in ['+', '-', '/', '*', '**']:
                break
            else:
                print("Erreur : entrez un caractère valide (+, -, *, /, **) : ")
        except ValueError:
            print()

    while True:
        try:
            num2 = float(input("Entrez un deuxième nombre valide : "))
            if operation == '/' and num2 == 0:
                print("Erreur : division par zéro. Veuillez entrer un autre nombre.")
            else:
                break
        except ValueError: 
            print("Erreur : entrez un caractère valide (nombre).")

    if operation == "+":
        resultat = num1 + num2
        historique += f"{num1} + {num2} = {resultat}\n"
    elif operation == "-":
        resultat = num1 - num2
        historique += f"{num1} - {num2} = {resultat}\n"
    elif operation == "*":
        resultat = num1 * num2
        historique += f"{num1} * {num2} = {resultat}\n"
    elif operation == "/":
        resultat = num1 / num2
        historique += f"{num1} / {num2} = {resultat}\n"
    elif operation == "**":
        resultat = num1 ** num2
        historique += f"{num1} ** {num2} = {resultat}\n"

    print(f"Résultat : {resultat}")

    while True:
        ask_historique = input("Voulez-vous afficher l'historique (y/n) ? ")
        if ask_historique.lower() == 'y':
            print(historique)
            break
        elif ask_historique.lower() == 'n':
            break
        else:
            print("Erreur : pour afficher l'historique entrez Oui (y) ou non (n).")

while True:
    calculatrice()
    while True:
        continuer = input("Continuer (y/n) ? ")
        if continuer.lower() == 'y':
            break
        elif continuer.lower() == 'n':
            exit()
        else:
            print("Erreur : pour continuer entrez oui (y) ou non (n)")