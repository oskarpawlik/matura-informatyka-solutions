file = open("trojki.txt", "r")
trojki = []
for line in file:
    trojki.append(line.strip().split())
for i in range(len(trojki)):
    trojki[i] = list(map(int, trojki[i]))
for i in range(len(trojki)):
    trojki[i].sort()


def is_triangle(l1, l2, l3):
    if l1**2 + l2**2 == l3**2:
        return True
    return False


dobre = []

for i in trojki:
    if is_triangle(i[0], i[1], i[2]):
        dobre.append(1)
    else:
        dobre.append(0)
for i in range(len(dobre) - 1):
    if dobre[i] == dobre[i + 1] == 1:
        print(trojki[i])
        print(trojki[i + 1])
