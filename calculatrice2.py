#variable historique en dehors de la fonction pour qu'elle ne soit pas écrasée à chaque boucle
historique = ""

def calculatrice():
    #permet l'appel de la variable externe à la fonction 
    global historique 
    #boucle infinie qui permet de rentrer les données de calcul à nouveau même en cas d'erreur
    while True: 
        try:
            num1 = float(input("Entrez un nombre valide : "))
            num2 = float(input("Entrez un deuxième nombre valide : "))
            operateur = input("Type d'opération (+, -, *, /, **) : ")
            #erreur de la division par 0
            if operateur == '/' and num2 == 0:
                print("Erreur : division par zéro. Veuillez entrer un autre nombre.")
            #erreur du mauvais caractère en opérateur
            elif operateur not in ['+', '-', '/', '*', '**']:
                print("Erreur : entrez un caractère valide (+, -, *, /, **) : ")
            else:
                break
        #erreur de caractère invalide dans le float qui ne prend que des nombres
        except ValueError:
            print("Erreur : entrez un caractère valide (nombre).")

   #dictionnaire qui donne l'opération à effectuer en fonction de l'opérateur 
    operations = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1 / num2,
        "**": num1 ** num2
    }
    
    resultat = operations[operateur]

    historique += f"{num1} {operateur} {num2} = {resultat}\n"

    print(f"Résultat : {resultat}")

    #boucle concernant l'historique, pour l'afficher ou non et l'effacer ou non
    while True:
        ask_historique = input("Voulez-vous afficher l'historique (y/n) ou l'effacer (d) ? ")
        if ask_historique.lower() == 'y':
            print(historique)
            break
        elif ask_historique.lower() == 'n':
            break
        elif ask_historique.lower() == 'd':
            historique = ""
            print("Historique effacé avec succès.")
            break
        else:
            print("Erreur : pour afficher l'historique entrez Oui (y) ou non (n).")

#boucle pour la continuité de la fonction, pour ne pas que l'histo soit écrasé à chaque redémarrage
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