file = open("sz.txt", "r")
szyfry = []
for i in file:
    szyfry.append(i.strip())

file = open("klucze2.txt", "r")
klucze = []
for i in file:
    klucze.append(i.strip())


def deszyfrowanie(szyfrogram, klucz):
    jawny = ""
    # jeśli długość ta sama
    roznica = 0
    if len(szyfrogram) == len(klucz):
        for i in range(len(szyfrogram)):
            roznica = ord(szyfrogram[i]) - (26 + ord(klucz[i]) - 90)
            if roznica < 65:
                roznica += 26
            jawny += chr(int(roznica))
    # jeśli długość różna
    else:
        i = 0
        while i < len(szyfrogram):
            roznica = ord(szyfrogram[i]) - (26 + ord(klucz[i % len(klucz)]) - 90)
            if roznica < 65:
                roznica += 26
            jawny += chr(int(roznica))
            i += 1
    return jawny


jawne = []
for i in range(len(szyfry)):
    jawne.append(deszyfrowanie(szyfry[i], klucze[i]))
print(jawne)
