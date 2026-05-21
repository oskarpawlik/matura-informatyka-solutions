file = open("dzialki.txt", "r")
dzialki = []
dzialka_temp = []
for line in file:
    if line != "\n":
        dzialka_temp.append(line.strip())
    else:
        dzialki.append(dzialka_temp)
        dzialka_temp = []


def max_plac(dzialka):
    bok = 1
    while True:
        for i in range(bok):
            for j in range(bok):
                if dzialka[i][j] == "X":
                    return bok - 1
        bok += 1


place = []

for i in dzialki:
    place.append(max_plac(i))
maksymalna = max(place)
print("maksymalny bok:", maksymalna)
for i in range(len(place)):
    if place[i] == maksymalna:
        print(i + 1)
