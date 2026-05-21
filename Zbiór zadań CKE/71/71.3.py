file = open("funkcja.txt", "r")
wsp = []
for i in file:
    wsp.append(i.strip().split())
for i in range(len(wsp)):
    for j in range(len(wsp[i])):
        wsp[i][j] = float(wsp[i][j])


def fx(wsp, x):
    return wsp[0] + wsp[1] * x + (wsp[2] * x**2) + (wsp[3] * x**3)


zakresy = [[0, 0.99999], [1, 1.99999], [2, 2.99999], [3, 3.99999], [4, 4.99999]]


def m_zerowe(wsp, zakresy):
    miejsca_zerowe = []
    for i in range(len(zakresy)):
        op = zakresy[i][0] + 0.00001
        while op - 0.00001 <= zakresy[i][1]:
            if (
                fx(wsp[i], op - 0.00001) * fx(wsp[i], op) > 0
                and fx(wsp[i], op) * fx(wsp[i], op + 0.00001) < 0
            ):
                miejsca_zerowe.append(round(op, 5))
            op += 0.00001
    return miejsca_zerowe


for i in m_zerowe(wsp, zakresy):
    print("m.zerowe:", i)
