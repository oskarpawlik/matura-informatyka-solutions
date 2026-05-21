import math

file = open("pierwsze.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())


def suma_cyfr(liczba):
    suma = 0
    for i in liczba:
        suma += int(i)
    return suma


def waga(liczba):
    waga = math.inf
    while waga > 9:
        waga = suma_cyfr(liczba)
        liczba = str(waga)
    if waga == 1:
        return True
    return False


for i in liczby:
    if waga(i):
        print(i)
