file = open("dane_obrazki.txt", "r")
obrazki = []
maly_obraz = []
for i in file:
    if i.strip() != "":
        maly_obraz.append(i.strip())
    if i.strip() == "":
        obrazki.append(maly_obraz)
        maly_obraz = []


def czy_rewers(obraz):
    biale = 0
    czarne = 0
    for linia in range(20):
        for piksel in range(20):
            if obraz[linia][piksel] == "1":
                czarne += 1
            else:
                biale += 1
    if czarne > biale:
        return True
    return False


def czarne_piksele(obraz):
    czarne = 0
    for linia in range(20):
        for piksel in range(20):
            if obraz[linia][piksel] == "1":
                czarne += 1
    return czarne


lista_czarne = []
counter = 0
for i in obrazki:
    lista_czarne.append(czarne_piksele(i))
    if czy_rewers(i):
        counter += 1
print("rewersy", counter)
print("najwiecej czarnych pikseli:", max(lista_czarne))
