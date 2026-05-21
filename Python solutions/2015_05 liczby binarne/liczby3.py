file = open("liczby.txt", "r")
liczby_binarne = []

for i in file:
    liczby_binarne.append(i.strip())
liczby_dziesietne = []

for i in liczby_binarne:
    liczby_dziesietne.append(int(i, 2))

maksymalna = max(liczby_dziesietne)
minimalna = min(liczby_dziesietne)
print("maksymalna wiersz", liczby_dziesietne.index(maksymalna) + 1)
print("minimalna wiersz", liczby_dziesietne.index(minimalna))
