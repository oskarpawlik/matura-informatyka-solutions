import math

file = open("liczby1.txt", "r")
liczby = []

for liczba in file:
    liczby.append(liczba.strip())
pary = []
for liczba in liczby:
    n = len(liczba)
    pary.append([int(liczba[0 : n // 2]), int(liczba[n // 2 :])])


def czy_wzg_pierwsza(x, y):
    if math.gcd(x, y) == 1:
        return True
    return False


counter = 0
for para in pary:
    if czy_wzg_pierwsza(para[0], para[1]):
        counter += 1
print(counter)
