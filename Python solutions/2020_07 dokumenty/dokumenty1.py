file = open("identyfikator.txt", "r")
identyfikatory_temp = []
for i in file:
    identyfikatory_temp.append(i.strip())
identyfikatory = []
for i in identyfikatory_temp:
    identyfikatory.append([i[0:3], i[3:]])


def suma(liczba):
    suma = 0
    for i in liczba:
        suma += int(i)
    return suma


sumy = []
for i in identyfikatory:
    sumy.append(suma(i[1]))
maksymalna = max(sumy)

for i in range(len(sumy)):
    if sumy[i] == maksymalna:
        print(identyfikatory[i])
