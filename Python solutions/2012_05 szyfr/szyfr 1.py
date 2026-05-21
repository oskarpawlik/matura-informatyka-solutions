file = open("tj.txt", "r")
jawne = []
for i in file:
    jawne.append(i.strip())

file = open("klucze1.txt", "r")
klucze = []
for i in file:
    klucze.append(i.strip())


def szyfrowanie(jawny, klucz):
    szyfrogram = ""
    # jeśli długość ta sama
    suma = 0
    if len(jawny) == len(klucz):
        for i in range(len(jawny)):
            suma = ord(jawny[i]) + 26 + ord(klucz[i]) - 90
            if suma > 90:
                suma -= 26
            szyfrogram += chr(int(suma))
    # jeśli długość różna
    else:
        i = 0
        while i < len(jawny):
            suma = ord(jawny[i]) + 26 + ord(klucz[i % len(klucz)]) - 90
            if suma > 90:
                suma -= 26
            szyfrogram += chr(int(suma))
            i += 1
    return szyfrogram


szyfrogramy = []
for i in range(len(jawne)):
    szyfrogramy.append(szyfrowanie(jawne[i], klucze[i]))
print(szyfrogramy)
