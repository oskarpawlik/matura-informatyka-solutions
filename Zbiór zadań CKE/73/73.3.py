file = open("tekst.txt", "r")
for i in file:
    slowa = i.strip().split(" ")
samogloski = ["A", "E", "I", "O", "U", "Y"]


def najdluzszy_ciag(slowo):
    ciag = []
    counter = 1
    for i in slowo:
        if i in samogloski:
            ciag.append(0)
            counter = 1
        else:
            ciag.append(counter)
            counter += 1
    return ciag


maksymalna_dl = []
for i in slowa:
    maksymalna_dl.append(max(najdluzszy_ciag(i)))

print("max dlugosc", max(maksymalna_dl))
print("ilosc slow", maksymalna_dl.count(max(maksymalna_dl)))

for i in slowa:
    if max(najdluzszy_ciag(i)) == max(maksymalna_dl):
        print(i)
        break
