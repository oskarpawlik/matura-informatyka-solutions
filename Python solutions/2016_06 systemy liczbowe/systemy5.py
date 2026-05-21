file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())


def into_dec(n):
    liczba = n[0 : len(n) - 1]
    system = int(n[-1])
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[len(liczba) - 1 - i]) * system**i
    return suma


liczby_dec = []
for i in liczby:
    liczby_dec.append(into_dec(i))
najwieksza = max(liczby_dec)
najmniejsza = min(liczby_dec)
print("najwieksza", liczby[liczby_dec.index(najwieksza)], najwieksza)
print("najmniejsza", liczby[liczby_dec.index(najmniejsza)], najmniejsza)
