file = open("funkcja.txt", "r")
wsp = []
for i in file:
    wsp.append(i.strip().split())
for i in range(len(wsp)):
    for j in range(len(wsp[i])):
        wsp[i][j] = float(wsp[i][j])


def funkcja(wsp, x):
    return wsp[0] + wsp[1] * x + (wsp[2] * x**2) + (wsp[3] * x**3)


zakresy = [[0, 0.99999], [1, 1.99999], [2, 2.99999], [3, 3.99999], [4, 4.99999]]


def maksymalna(wsp, zakresy):
    maximum = 0
    max_op = 0
    for i in range(len(zakresy)):
        op = zakresy[i][0]
        while op <= zakresy[i][1]:
            if maximum < funkcja(wsp[i], op):
                maximum = funkcja(wsp[i], op)
                max_op = op
            op += 0.00001
    return [maximum, max_op]


print(
    round(maksymalna(wsp, zakresy)[0], 5),
    "dla x:",
    round(maksymalna(wsp, zakresy)[1], 3),
)
