file = open("bin.txt", "r")
liczby1 = []
for line in file:
    liczby1.append(line.strip())
liczby_dec = []

for i in liczby1:
    liczby_dec.append(int(i, 2))

liczby2 = []
for i in liczby_dec:
    nowa = i // 2
    liczby2.append(bin(nowa)[2::])

for i in range(len(liczby2)):
    liczba = liczby2[i].zfill(len(liczby1[i]))
    liczby2[i] = liczba


def XOR(a, b):
    res = ""
    for i in range(len(a)):
        if a[i] == "1" and b[i] == "1":
            res = res + "0"
        elif a[i] == "0" and b[i] == "0":
            res = res + "0"
        else:
            res = res + "1"
    return res


for i in range(len(liczby2)):
    print(XOR(liczby2[i], liczby1[i]))
