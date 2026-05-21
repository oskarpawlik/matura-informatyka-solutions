file = open("dane_6_3.txt", "r")
data = []
for line in file:
    parts = line.strip().split()
    if len(parts) == 2:
        data.append(parts)


def czy_dobrze(slowo, szyfr):
    przesuniecia = []
    przesuniecie = 0
    for i in range(len(slowo) - 1):
        if ord(slowo[i]) < ord(szyfr[i]):
            przesuniecie = ord(szyfr[i]) - ord(slowo[i])
        elif ord(slowo[i]) > ord(szyfr[i]):
            przesuniecie = 90 - ord(slowo[i]) + ord(szyfr[i]) - 65 + 1
        przesuniecia.append(przesuniecie)
    if len(set(przesuniecia)) == 1:
        return True
    return False


for i in range(len(data)):
    if czy_dobrze(data[i][0], data[i][1]) == False:
        print(data[i][0])
