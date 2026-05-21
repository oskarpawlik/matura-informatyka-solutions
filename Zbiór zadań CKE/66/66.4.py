file = open("trojki.txt", "r")
trojki = []
for line in file:
    trojki.append(line.strip().split())
for i in range(len(trojki)):
    trojki[i] = list(map(int, trojki[i]))
for i in range(len(trojki)):
    trojki[i].sort()


def is_triangle(l1, l2, l3):
    if l1 + l2 > l3:
        return True
    return False


trojkaty = []
for i in trojki:
    if is_triangle(i[0], i[1], i[2]):
        trojkaty.append(1)
    else:
        trojkaty.append(0)
ciag = [trojkaty[0]]

for i in range(1, len(trojkaty)):
    if trojkaty[i] == 0:
        ciag.append(0)
    else:
        ciag.append(ciag[i - 1] + trojkaty[i])

print(max(ciag))
print(int(sum(trojkaty)))
