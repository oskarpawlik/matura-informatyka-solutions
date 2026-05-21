file = open("dane_6_1.txt", "r")
data = []
for i in file:
    data.append(i.strip())


def szyfrowanie(napis, k):
    wynik = ""
    litera = 0
    k = k % 26
    for i in napis:
        litera = ord(i) + k
        if litera > 90:
            litera = litera - 26
        wynik += chr(litera)
    return wynik


for i in data:
    print(szyfrowanie(i, 107))
