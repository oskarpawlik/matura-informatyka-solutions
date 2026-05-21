file = open("dane_ulamki.txt", "r")
ulamki = []
for i in file:
    ulamki.append(i.split())
for i in range(len(ulamki)):
    ulamki[i][0] = int(ulamki[i][0])
    ulamki[i][1] = int(ulamki[i][1])
wartosci = []
for i in range(len(ulamki)):
    wartosci.append(ulamki[i][0] / ulamki[i][1])
print(ulamki[wartosci.index(min(wartosci))])
