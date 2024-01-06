n= int(input("entrez un nombre:"))
produit=1
nb=1
bool=int(input("veillez choisir la boucle (tapez 1 pour for), (tapez 0 pour while) :"))
if bool==1:
    for i in range(1,n+1):
        produit*=i
        print(f"le produit est : {produit}")
        if i==n:
            print(f"la factorielle  est : {produit}")
elif bool==0:
    while nb!=n+1:
        produit*=nb
        print(f"le produit est : {produit}")
        if nb == n:
            print(f"la factorielle  est : {produit}")
        nb+=1
