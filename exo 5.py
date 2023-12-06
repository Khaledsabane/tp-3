def calcul_prix_location(heure_debut, heure_fin):


    if heure_debut < 0 or heure_fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !\n")
        return
    if heure_debut == heure_fin:
        print("Attention ! L'heure de fin est identique à l'heure de début.\n")
        return
    elif heure_debut > heure_fin:
        print("Attention ! Le début de la location est après la fin.\n")
        return


    if heure_debut >= 0 and heure_fin <= 7 or heure_debut >= 17 and heure_fin <= 24:
        prix = (heure_fin - heure_debut) * 1
    else:
        prix = (heure_fin - heure_debut) * 2

    print(f"Le coût de la location est de {prix} euros.")

heure_debut = int(input("Veuillez entrer l'heure de début de location : "))
heure_fin = int(input("Veuillez entrer l'heure de fin de location : "))


calcul_prix_location(heure_debut, heure_fin)
