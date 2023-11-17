import time
n = int(input("saisir un nombre entier n positif:"))
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)


import time
n = int(input("saisir un nombre entier n positif:"))
while n >=0:
    print(n)
    n -= 1
    time.sleep(1)