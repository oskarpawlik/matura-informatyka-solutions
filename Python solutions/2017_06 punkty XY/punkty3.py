file = open("punkty.txt", "r")
punkty = []
for i in file:
    punkty.append(i.strip().split())
for i in range(len(punkty)):
    punkty[i] = list(map(int, punkty[i]))


def odleglosc(x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5


max_odleglosc = 0
X = 0
Y = 0
for i in range(len(punkty) - 1):
    for j in range(1 + i, len(punkty)):
        if (
            odleglosc(punkty[i][0], punkty[i][1], punkty[j][0], punkty[j][1])
            > max_odleglosc
        ):
            X = punkty[i][0], punkty[i][1]
            Y = punkty[j][0], punkty[j][1]
            max_odleglosc = odleglosc(
                punkty[i][0], punkty[i][1], punkty[j][0], punkty[j][1]
            )
print(round(max_odleglosc))
print(X, Y)
