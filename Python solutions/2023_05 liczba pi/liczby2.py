file = open("pi.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())

fragmenty = []

for i in range(len(liczby) - 1):
    fragmenty.append(int(liczby[i] + liczby[i + 1]))

unikalne = []
for i in range(0, 100):
    unikalne.append(i)

ilosc = []


for i in unikalne:
    ilosc.append(fragmenty.count(i))
minimalna = min(ilosc)
minimalna_index = ilosc.index(minimalna)
maksymalna = max(ilosc)
maksymalna_index = ilosc.index(maksymalna)

print("wyst i minimalna")
print(unikalne[minimalna_index], minimalna)
print("wyst i maksymalna")
print(unikalne[maksymalna_index], maksymalna)
