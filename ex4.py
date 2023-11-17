factorielle=1
n = int(input("saisir un nombre :"))
for i in range(1, n+1):
    factorielle *=i
print(f"le factorielle est:{factorielle}")