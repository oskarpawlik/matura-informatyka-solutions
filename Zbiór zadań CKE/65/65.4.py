file = open("dane_ulamki.txt", "r")
ulamki = []
for i in file:
    ulamki.append(i.split())
for i in range(len(ulamki)):
    ulamki[i][0] = int(ulamki[i][0])
    ulamki[i][1] = int(ulamki[i][1])
b = 2 * 2 * 3 * 3 * 5 * 5 * 7 * 7 * 13
liczniki = []


def rozszerzanie(licznik, mianownik):
    ile_razy = b / mianownik
    return ile_razy * licznik


for i in ulamki:
    liczniki.append(rozszerzanie(i[0], i[1]))
print(int(sum(liczniki)))
