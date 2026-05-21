file = open("napisy.txt", "r")
napisy = []
for i in file:
    napisy.append(i.strip().split())


def dl_zakonczenia(napis1, napis2):
    krotszy = min(len(napis1), len(napis2))
    dlugosc = 0
    for i in range(-1, -krotszy, -1):
        if napis1[i] == napis2[i]:
            dlugosc += 1
        else:
            break
    return dlugosc


dlugosci = []
for napis in napisy:
    dlugosci.append(dl_zakonczenia(napis[0], napis[1]))
print("max dlugosc", max(dlugosci))

for i in range(len(dlugosci)):
    if dlugosci[i] == max(dlugosci):
        print(napisy[i])
