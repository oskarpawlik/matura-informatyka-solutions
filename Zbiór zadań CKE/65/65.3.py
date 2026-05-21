import math

file = open("dane_ulamki.txt", "r")
ulamki = []
for i in file:
    ulamki.append(i.split())
for i in range(len(ulamki)):
    ulamki[i][0] = int(ulamki[i][0])
    ulamki[i][1] = int(ulamki[i][1])


def czynnkiki(n):
    czynnki = []
    i = 2
    while n != 1:
        if n % i == 0:
            czynnki.append(i)
            n = n // i
            i = 1
        i += 1
    return czynnki


def czy_nieskracalne(czynniki1, czynniki2):
    for i in czynniki1:
        for j in czynniki2:
            if i == j:
                return False
    return True


def skracanie(czynniki1, czynniki2, licznik, mianownik):
    wspolne = 1
    l1 = 1
    l2 = 1
    for i in czynniki1:
        l1 *= i
    for i in czynniki2:
        l2 *= i
    wspolne = math.gcd(l1, l2)
    return [int(licznik / wspolne), int(mianownik / wspolne)]


suma = 0
nieskracalne = []
for ulamek in ulamki:
    if czy_nieskracalne(czynnkiki(ulamek[0]), czynnkiki(ulamek[1])):
        nieskracalne.append(ulamek)
    else:
        nieskracalne.append(
            skracanie(czynnkiki(ulamek[0]), czynnkiki(ulamek[1]), ulamek[0], ulamek[1])
        )
suma = 0
for i in nieskracalne:
    suma += i[0]
print(suma)
