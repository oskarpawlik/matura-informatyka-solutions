file1 = open("kody.txt", "r")
liczby = []
for i in file1:
    liczby.append(i.strip())
kody = []

file2 = open("cyfra_kodkreskowy.txt", "r")
for i in file2:
    kody.append(i.strip().split())


def nieparzyste(N):
    suma = 0
    for i in range(0, len(N), 2):
        suma += int(N[i])
    return suma


def parzyste(N):
    suma = 0
    for i in range(1, len(N), 2):
        suma += int(N[i])
    return suma


def kontrolna(liczba):
    return (10 - ((3 * parzyste(liczba) + nieparzyste(liczba)) % 10)) % 10


for i in liczby:
    print(kontrolna(i), i)
