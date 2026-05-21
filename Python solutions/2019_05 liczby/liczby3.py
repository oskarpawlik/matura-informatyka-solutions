import math

file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(int(i))


def najmniejszy_dzielnik(n):
    if n < 2:
        return n
    for i in range(2, n + 1):
        if n % i == 0:
            return i


najmniejsze_dzielniki = []
for i in liczby:
    najmniejsze_dzielniki.append(najmniejszy_dzielnik(i))

ciag = [1] * len(liczby)
for i in range(0, len(liczby) - 1):
    if najmniejsze_dzielniki[i] == najmniejsze_dzielniki[i + 1]:
        ciag[i + 1] = ciag[i] + 1

maksymalna = max(ciag)
indeks = ciag.index(maksymalna)
ciag_res = []

for i in range(indeks - maksymalna + 1, indeks + 1):
    ciag_res.append(liczby[i])
nwd = ciag_res[0]

for i in range(1, len(ciag_res)):
    nwd = math.gcd(nwd, ciag_res[i])

print("dl ciagu", maksymalna)
print("poczotek", liczby[indeks - maksymalna + 1])
print("nwd", nwd)
