file = open("funkcja.txt", "r")
wsp = []
for i in file:
    wsp.append(i.strip().split())
for i in range(len(wsp)):
    for j in range(len(wsp[i])):
        wsp[i][j] = float(wsp[i][j])


def funkcja(wsp, x):
    return wsp[0] + wsp[1] * x + (wsp[2] * x**2) + (wsp[3] * x**3)


print(round(funkcja(wsp[1], 1.5), 5))
