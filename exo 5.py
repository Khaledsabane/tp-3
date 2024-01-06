debut_location = int(input("Donnez l’heure de début de la location : "))
fin_location = int(input("Donnez l’heure de fin de la location  : "))
somme_heures_1euro=0
somme_heures_2euro=0
if debut_location<0 or fin_location>24  :
    print(f"Les heures doivent être comprises entre 0 et 24 ! ")
elif debut_location==fin_location:
    print(f"Attention ! l’heure de fin est identique à l’heure de début.")
elif debut_location>fin_location :
    print(f"Attention ! le début de la location est après la fin ... ")
else:
    for heure in range(debut_location,fin_location):
        if heure < 7 or (heure >= 17 and heure <= 24):
            somme_heures_1euro+=1
        elif heure>=7 and heure<17:
            somme_heures_2euro += 1
    print(f"Vous avez loué votre vélo pendant")
    if somme_heures_1euro>0:
        print(f"{somme_heures_1euro} heure(s) au tarif horaire de 1.0 euro(s) ")
    if somme_heures_2euro > 0:
        print(f"{somme_heures_2euro} heure(s) au tarif horaire de 2.0 euro(s)")

    print(f"Le montant total à payer est de {(somme_heures_1euro+somme_heures_2euro*2)} euro(s)")
