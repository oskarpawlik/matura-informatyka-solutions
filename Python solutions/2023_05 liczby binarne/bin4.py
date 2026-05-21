file = open("bin.txt", "r")
liczby1 = []
for line in file:
    liczby1.append(line.strip())
liczby_dec = []

for i in liczby1:
    liczby_dec.append(int(i, 2))

liczby2 = []
for i in liczby_dec:
    nowa = i // 2
    liczby2.append(nowa)

liczby_xor = []
for i in range(len(liczby2)):
    liczba = liczby2[i] ^ liczby_dec[i]
    liczby_xor.append(bin(liczba)[2::])
print(liczby_xor)
