file = open("dane_obrazki.txt", "r")
obrazki = []
maly_obraz = []
for i in file:
    if i.strip() != "":
        maly_obraz.append(i.strip())
    if i.strip() == "":
        obrazki.append(maly_obraz)
        maly_obraz = []


def czy_rekurencyjny(obraz):
    c1 = ""
    c2 = ""
    c3 = ""
    c4 = ""
    for linia in range(0, len(obraz) - 1):
        if linia < 10:
            c1 += str(obraz[linia][0:10])
            c2 += str(obraz[linia][10:20])
        else:
            c3 += str(obraz[linia][0:10])
            c4 += str(obraz[linia][10:20])
    if c1 == c2 == c3 == c4:
        return True
    else:
        return False


counter = 0
for i in obrazki:
    if czy_rekurencyjny(i):
        counter += 1
print(counter)

for obraz in obrazki:
    if czy_rekurencyjny(obraz):
        for linia in range(0, len(obraz) - 1):
            print(obraz[linia][0:20])
        break
