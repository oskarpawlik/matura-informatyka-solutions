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
    wiersz_numer = 0
    for i in range(20):
        wiersz = obraz[i][0:20]
        jedynki = wiersz.count("1")
        if jedynki % 2 != 0:
            poprawny = "1"
        else:
            poprawny = "0"
        if obraz[i][-1] != poprawny:
            zle += 1
            wiersz_numer = i + 1
    return zle, wiersz_numer


def zle_kolumny(obraz):
    zle = 0
    jedynki = 0
    kolumna_numer = 0
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
            kolumna_numer = i + 1
        jedynki = 0
    return zle, kolumna_numer


for i in range(len(obrazki)):
    j = obrazki[i]
    if zle_wierszse(j)[0] == 1 and zle_kolumny(j)[0] == 1:
        print(i + 1, zle_wierszse(j)[1], zle_kolumny(j)[1])
    elif zle_wierszse(j)[0] == 1 and zle_kolumny(j)[0] == 0:
        print(i + 1, zle_wierszse(j)[1], 21)
    elif zle_wierszse(j)[0] == 0 and zle_kolumny(j)[0] == 1:
        print(i + 1, 21, zle_kolumny(j)[1])
