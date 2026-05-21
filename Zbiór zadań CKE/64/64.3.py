file = open("dane_obrazki.txt", "r")
obrazki = []
maly_obraz = []
for i in file:
    if i.strip() != "":
        maly_obraz.append(i.strip())
    if i.strip() == "":
        obrazki.append(maly_obraz)
        maly_obraz = []


def zle_wierszse(obraz):
    zle = 0
    for i in range(20):
        wiersz = obraz[i][0:20]
        jedynki = wiersz.count("1")
        if jedynki % 2 != 0:
            poprawny = "1"
        else:
            poprawny = "0"
        if obraz[i][-1] != poprawny:
            zle += 1
    return zle


def zle_kolumny(obraz):
    zle = 0
    jedynki = 0
    for i in range(20):
        for j in range(20):
            if obraz[j][i] == "1":
                jedynki += 1
        if jedynki % 2 != 0:
            poprawny = "1"
        else:
            poprawny = "0"
        if obraz[-1][i] != poprawny:
            zle += 1
        jedynki = 0
    return zle


poprawne = 0
naprawialne = 0
nienaprawialne = 0
max_zlych = 0
for i in obrazki:
    wiersz = zle_wierszse(i)
    kolumny = zle_kolumny(i)
    suma = wiersz + kolumny
    if suma > max_zlych:
        max_zlych = suma

    if wiersz == kolumny == 0:
        poprawne += 1
    elif wiersz < 2 and kolumny < 2:
        naprawialne += 1
    else:
        nienaprawialne += 1
print("poprawne", poprawne)
print("naprawialne", naprawialne)
print("nienaprawialne", nienaprawialne)
print("max_zlych", max_zlych)
