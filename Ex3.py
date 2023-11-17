import random
p = random.randint(0, 100)
i=0
x = int(input("saisir x:"))


while x !=p:
    i += 1
    if x < p:
        print("la valeur est plus grande")
    else:
        print("la valeur est plus petite")
    x = int(input("saisir x:"))

print(f"vous avez réussi avec le nombre {x} avec {i} tentatives")