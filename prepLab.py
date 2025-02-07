#3 bloc de condition complet
# 3 entre utilisateur
# 1 opérateur logique
# imprimer le résultat

print("inscrivez 3 nombres")
# Demander trois entrées utilisateur
input1 = float(input("Entrez le premier nombre : "))
input2 = float(input("Entrez le deuxième nombre : "))
input3 = float(input("Entrez le troisième nombre : "))

# Utiliser un opérateur logique pour vérifier les conditions
if input1 > input2 and input1 > input3:
    result = f"Le premier nombre {input1} est le plus grand."
elif input2 > input1 and input2 > input3:
    result = f"Le deuxième nombre {input2} est le plus grand."
else:
    result = f"Le troisième nombre {input3} est le plus grand."
if input1 == input2 and input2 == input3: # si les 3 nombres sont égaux
    result = "Les trois nombres sont égaux, prépare toi."
print(result)
input4 = str(input("Voulez vous jouer a roche papier sciscaux? (oui/non) : "))
if input4 == "non":
    print("Au revoir!")
    exit() #ferme le programme si "non" est entré
elif input4 == "oui": # si "oui" est entré, le programme continue
    print("Choisissez entre roche, papier ou ciseaux.") # roche papier ciseaux classique, (une partie)
else:
    import random # dit a l'ordi de choisir une valeur au hasard q'on vas définir

    options = ["roche", "papier", "ciseaux"] # répertoire des choix possibles de l'ordinateur et utilisateur

    user_choice = input("Choose roche, papier, or ciseaux:") # demande a l'utilisateur de choisir
    computer_choice = random.choice(options)

    print("You chose: ", user_choice) # affiche ce que l'utilisateur a choisi
    print("Computer chose: ", computer_choice) # affiche ce que l'ordinateur a choisi
# condition pour déterminer le gagnant
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "roche" and computer_choice == "ciseaux":
        print("You win!")
    elif user_choice == "papier" and computer_choice == "roche":
        print("You win!")
    elif user_choice == "ciseaux" and computer_choice == "papier":
        print("You win!")
    else:
        print("Computer wins!")
# fin du programme