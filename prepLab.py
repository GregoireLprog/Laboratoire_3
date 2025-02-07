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
if input1 == input2 and input2 == input3:
    result = "Les trois nombres sont égaux, prépare toi."
print(result)
input4 = str(input("Voulez vous jouer a roche papier sciscaux? (oui/non) : "))
if input4 == "non":
    print("Au revoir!")
    exit()
elif input4 == "oui":
    print("Choisissez entre roche, papier ou ciseaux.")
else:
    import random

    options = ["Rock", "Paper", "Scissors"]

    user_choice = input("Choose Rock, Paper, or Scissors: ")
    computer_choice = random.choice(options)

    print("You chose: ", user_choice)
    print("Computer chose: ", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
    else:
        print("Computer wins!")

# Imprimer le résultat