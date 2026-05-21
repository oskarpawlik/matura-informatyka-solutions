import math

A = [2, -32 - 2 / 3]
B = [10, -32 - 2 / 3]
C = [10, 2, 19 + 61 / 125]
D = [2, 19 + 61 / 125]


def dl_odcinka(A, B):
    dlugosc = (((A[0] - B[0]) ** 2) + ((A[1] - B[1]) ** 2)) ** (1 / 2)
    return dlugosc


pole_calosci = dl_odcinka(A, B) * dl_odcinka(A, D)


def pole_pod_wykresem(start, koniec, funkcja):

    suma = 0
    while start <= koniec:
        suma += (
            (abs(funkcja(start)) + abs(funkcja(start + (1 / 1000)))) * 1 / 1000
        ) / 2
        start += 1 / 1000
    return suma


def GX(x):
    return -(x**3 / 30) + (x / 20) + 1 / 6


def FX(x):
    return (x**4 / 500) - (x**2 / 200) - (3 / 250)


pozostaly_material = pole_calosci - (
    pole_pod_wykresem(2, 10, GX) + pole_pod_wykresem(2, 10, FX)
)
szerokosci = []
i = 10
while i != 2:
    i = i - 0.25
    szerokosci.append(i)
metry = 0
for i in szerokosci:
    pas = dl_odcinka([i, GX(i)], [i, FX(i)])

    if pozostaly_material - math.floor(pas) * 0.25 > 0:
        metry += math.floor(pas)
        pozostaly_material -= math.floor(pas) * 0.25
print(metry)
