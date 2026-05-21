file = open("dane.txt", "r")
ciag = []
for line in file:
    for i in line:
        ciag.append(i)
liczby = []

liczba = ""
for i in range(len(ciag)):
    if ciag[i].isdigit():
        liczba += ciag[i]
    elif len(liczba) != 0:
        liczby.append(liczba)
        liczba = ""

numery_tel = []
for liczba in liczby:
    if len(liczba) == 9:
        numery_tel.append(liczba)

ile_cyfr = []

for i in numery_tel:
    ile_cyfr.append(len(set(i)))
min_cyfr = min(ile_cyfr)

for i in range(len(ile_cyfr)):
    if ile_cyfr[i] == min_cyfr:
        print(numery_tel[i])
