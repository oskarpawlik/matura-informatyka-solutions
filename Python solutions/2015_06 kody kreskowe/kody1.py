file = open("kody.txt", "r")
kody = []
for i in file:
    kody.append(i.strip())


def nieparzyste(N):
    suma = 0
    for i in range(0, len(N), 2):
        suma += int(N[i])
    return suma


def parzyste(N):
    suma = 0
    for i in range(1, len(N), 2):
        suma += int(N[i])
    return suma


for i in kody:
    print(parzyste(i), nieparzyste(i))
