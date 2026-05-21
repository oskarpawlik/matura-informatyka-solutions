file = open("dane4.txt", "r")
ciag = []
for i in file:
    ciag.append(i.strip())


def luki(ciag):
    luki = [1] * len(ciag)

    for i in range(len(ciag) - 2):
        dl = 1
        for j in range(i, len(ciag) - 2):
            if abs(int(ciag[j + 2]) - int(ciag[j + 1])) == abs(
                int(ciag[j]) - int(ciag[j + 1])
            ):
                dl += 1
            else:
                break
        dl += 1
        luki[i] = dl
    return luki


luki_ciag = luki(ciag)

max_luki = max(luki_ciag)
index_ciagu = ciag.index(max(ciag))
print(ciag[index_ciagu])
print(index_ciagu)
for i in luki_ciag:
    if i == max_luki:
        print("tak")
