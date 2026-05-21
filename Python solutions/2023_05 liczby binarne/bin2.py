file = open("bin.txt", "r")
liczby = []
for line in file:
    liczby.append(line.strip())

liczby_dec = []
for i in liczby:
    liczby_dec.append(int(i, 2))
maksymalna = max(liczby_dec)
maksymalna_indeks = liczby_dec.index(maksymalna)
print(liczby[maksymalna_indeks])
