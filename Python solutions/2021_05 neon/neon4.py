file = open("instrukcje.txt", "r")
instrukcje = []
for i in file:
    instrukcje.append(i.strip().split())


def DOPISZ(napis, litera):
    return napis + litera


def ZMIEN(napis, litera):
    napis = napis[0 : len(napis) - 1] + litera
    return napis


def USUN(napis, znak):
    return napis[0 : len(napis) - 1]


def PRZESUN(napis, litera):
    numer = ord(litera)
    numer += 1
    if numer == 91:
        numer = 65
    for i in range(len(napis)):
        if napis[i] == litera:
            napis = napis[0:i] + chr(numer) + napis[i + 1 :]
            return napis


napis = ""
for instrukcja in instrukcje:
    if instrukcja[0] == "DOPISZ":
        napis = DOPISZ(napis, instrukcja[1])
    elif instrukcja[0] == "ZMIEN":
        napis = ZMIEN(napis, instrukcja[1])
    elif instrukcja[0] == "USUN":
        napis = USUN(napis, instrukcja[1])
    elif instrukcja[0] == "PRZESUN":
        napis = PRZESUN(napis, instrukcja[1])
print(napis)
