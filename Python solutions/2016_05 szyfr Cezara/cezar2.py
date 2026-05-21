file = open("dane_6_2.txt", "r")
data = []
for line in file:
    parts = line.strip().split()
    if len(parts) == 2:
        data.append(parts)


def deszyfrowanie(napis, k):
    wynik = ""
    k = int(k) % 26
    for i in napis:
        litera = ord(i) - k
        if litera < 65:
            litera += 26
        wynik += chr(litera)
    return wynik


for i in range(len(data)):
    print(deszyfrowanie(data[i][0], data[i][1]))
