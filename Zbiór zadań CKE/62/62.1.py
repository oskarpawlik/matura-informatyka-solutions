file = open("liczby1.txt", "r")
liczby = []
for line in file:
    liczby.append(line.strip())
liczby_dec = []
for i in range(len(liczby)):
    liczby_dec.append(int(liczby[i], 8))
maksymalna = max(liczby_dec)
minimalna = min(liczby_dec)

print("maksymalna", liczby[liczby_dec.index(maksymalna)])
print("minimalna", liczby[liczby_dec.index(minimalna)])
