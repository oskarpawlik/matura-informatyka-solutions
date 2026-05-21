file = open("liczby2.txt", "r")
liczby = []

for liczba in file:
    liczby.append(liczba.strip())
kwadraty = []
for liczba in liczby:
    kwadraty.append(str(int(liczba) * int(liczba)))
stopnie = []


def stopien_kaprekara(n, kwadrat):
    stopien = 0
    for i in range(1, len(kwadrat) - 1):
        if int(kwadrat[0:i:]) + int(kwadrat[i::]) <= int(n):
            stopien += 1
    return stopien


for i in range(len(kwadraty)):
    stopnie.append(stopien_kaprekara(liczby[i], kwadraty[i]))

maxstopien = max(stopnie)
maxindex = stopnie.index(maxstopien)
print(maxstopien)
print(liczby[maxindex])
