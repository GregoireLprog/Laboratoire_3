#3 bloc de condition complet
# 3 entre utilisateur
# 1 opérateur logique
# imprimer le résultat

print("inscrivez 3 nombres")
# Demander trois entrées utilisateur
input1 = int(input("Entrez le premier nombre : "))
input2 = int(input("Entrez le deuxième nombre : "))
input3 = int(input("Entrez le troisième nombre : "))

# Utiliser un opérateur logique pour vérifier les conditions
if input1 > input2 and input1 > input3:
    result = f"Le premier nombre {input1} est le plus grand."
elif input2 > input1 and input2 > input3:
    result = f"Le deuxième nombre {input2} est le plus grand."
else:
    result = f"Le troisième nombre {input3} est le plus grand."

# Imprimer le résultat
print(result)
