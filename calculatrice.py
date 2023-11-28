def calculatrice():
    while True:
        try:
            num1 = float(input("Entrez un nombre valide : "))
            break
        except ValueError: 
            print("Entrez un autre nombre : ")

    while True:
        try:
            operation = input("Type d'opération : ")
            if operation == '+' or operation == '-' or operation == '/' or operation == '*' or operation == '**':
                break
        except ValueError: 
            print("Entrez un opérateur valide : ")

    while True:
        try:
            num2 = float(input("Entrez un deuxième nombre valide : "))
            if operation == '/' and num2 == 0:
                print("Erreur : division par zéro. Veuillez entrer un autre nombre.")
            else:
                break
        except ValueError: 
            print("Entrez un autre nombre.")

    if operation == "+":
        print (num1+num2)
    elif operation == "-":
        print (num1-num2)
    elif operation == "*":
        print (num1*num2)
    elif operation == "/":
        print (num1/num2)
    elif operation == "**":
        print(num1**num2)

calculatrice()