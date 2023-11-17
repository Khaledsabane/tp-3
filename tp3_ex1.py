#question a
N=int(input("entrez N:"))
somme=0
for i in range (N + 1):
    somme += i

print(f"la somme de {N} est {somme}")


#question b
x=int(input("entrez x:"))
while x != 100:
    print("entrez une nouvelle valeur: ")


#question c
nbr_10 = 0
nbr_15 = 0
nbr_20 = 0

for i in range (10):
    D = int(input("entrez 10 valeurs:"))
    while (D<0 or D>20):
        D = int(input("entrez D:"))
    if D < 10:
     nbr_10 += 1
    elif D > 15:
     nbr_15 += 1
    else:
     nbr_20 += 1
    print("")
print(f"nombre de note inférieur à 10 est {nbr_10}")
print(f"Le nombre de valeurs supérieur ou égale à 10 et inférieur strictement à 15 est {nbr_15}")
print(f"Le nombre de valeurs supérieur ou égale à 15 {nbr_20}")

print("-------------------------")
#question d

j = int(input("entrez j:"))
som=0
m=0
while som <= j:
    m += 1
    som += m

print(f"la somme est {som}")
print(f"le nombre le plus grand esr {j}")

#Exercice 2
