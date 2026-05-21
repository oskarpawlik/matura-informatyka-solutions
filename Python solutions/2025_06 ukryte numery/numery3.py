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

for i in numery_tel:
    if i[0] == "5":
        print(i)
