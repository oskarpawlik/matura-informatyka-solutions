file = open("dron.txt", "r")
wsp = []
for line in file:
    para = [int(x) for x in line.split()]
    wsp.append(para)


def srodek(x1, y1, x2, y2):
    return [(x1 + x2) / 2, (y1 + y2) / 2]


pozycje = [[0, 0]]
poz_x = 0
poz_y = 0
for para in wsp:
    poz_x += para[0]
    poz_y += para[1]
    pozycje.append([poz_x, poz_y])

for i in range(0, len(pozycje) - 1):
    for j in range(1 + i, len(pozycje)):
        if (
            srodek(pozycje[i][0], pozycje[i][1], pozycje[j][0], pozycje[j][1])
            in pozycje
        ):
            print(
                pozycje[i][0],
                pozycje[i][1],
                srodek(pozycje[i][0], pozycje[i][1], pozycje[j][0], pozycje[j][1]),
                pozycje[j][0],
                pozycje[j][1],
            )
