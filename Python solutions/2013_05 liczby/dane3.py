file = open("dane.txt", "r")
osemkowe = []
for i in file:
    osemkowe.append(i.strip())


def dziesiatkowe(num):
    return int(num, 8)


def warunek(num):
    for i in range(len(num) - 1):
        if num[i] > num[i + 1]:
            return False
    return True


spelniajace_warunek = []


for num in osemkowe:
    if warunek(num):
        spelniajace_warunek.append(num)

decymalne = []
for i in spelniajace_warunek:
    decymalne.append(dziesiatkowe(i))
maksymalna = max(decymalne)
minimalna = min(decymalne)
print(len(spelniajace_warunek))
print(spelniajace_warunek[decymalne.index(minimalna)])
print(spelniajace_warunek[decymalne.index(maksymalna)])
