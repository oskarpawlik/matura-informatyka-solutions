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


counter = 0
for liczba in liczby:
    if liczba[:2] == "50":
        counter += 1

print(counter)
