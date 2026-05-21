file = open("dane_geny.txt", "r")
genotypy = []
for i in file:
    genotypy.append(i.strip())
gatunki = []
for i in genotypy:
    gatunki.append(len(i))
ilosc = len(set(gatunki))
print("ilosc gatunkow", ilosc)
gatunki = sorted(gatunki)
sizes = []
counter = 1
for i in range(len(gatunki) - 1):
    if gatunki[i] == gatunki[i + 1]:
        counter += 1
    else:
        sizes.append(counter)
        counter = 1
print("najwiekszy gatunek", max(sizes))
