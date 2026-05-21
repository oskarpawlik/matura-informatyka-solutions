file = open("dzialki.txt", "r")
dzialki = []
dzialka_temp = []
for line in file:
    if line != "\n":
        dzialka_temp.append(line.strip())
    else:
        dzialki.append(dzialka_temp)
        dzialka_temp = []

dzialki_reversed = []


def odwracanie(dzialka):
    nowa = []
    for i in range(len(dzialka) - 1, -1, -1):
        nowa.append(dzialka[i][::-1])
    return nowa


for dzialka in dzialki:
    dzialki_reversed.append(odwracanie(dzialka))
for i in range(len(dzialki_reversed)):
    for j in range(1 + i, len(dzialki_reversed)):
        if dzialki_reversed[i] == dzialki[j] and j != i:
            print(i + 1, j + 1)
