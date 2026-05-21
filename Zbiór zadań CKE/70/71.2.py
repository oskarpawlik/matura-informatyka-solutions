import math

A = [2, -32 - 2 / 3]
B = [10, -32 - 2 / 3]
C = [10, 19 + 61 / 125]
D = [2, 19 + 61 / 125]


def dl_odcinka(A, B):
    dlugosc = (((A[0] - B[0]) ** 2) + ((A[1] - B[1]) ** 2)) ** (1 / 2)
    return dlugosc


Pole_calosci = dl_odcinka(A, B) * dl_odcinka(A, D)

lewa = dl_odcinka(A, D)
gora = dl_odcinka(D, C)
dol = dl_odcinka(A, B)


def GX(x):
    return -(x**3 / 30) + (x / 20) + 1 / 6


def FX(x):
    return (x**4 / 500) - (x**2 / 200) - (3 / 250)


x = [2]
for i in range(0, 1000):
    x.append(x[-1] + (8 / 1000))


def obwod(x, funkcja):
    suma = 0
    for i in range(0, len(x) - 1):
        suma += dl_odcinka([x[i], funkcja(x[i])], [x[i + 1], funkcja(x[i + 1])])
    return suma


obwod_zaslony = gora + lewa + dol + obwod(x, FX) + obwod(x, GX)
print(math.ceil(obwod_zaslony))
