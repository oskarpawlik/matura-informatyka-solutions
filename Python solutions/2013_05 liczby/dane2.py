file = open("dane.txt", "r")
osemkowe = []
for i in file:
    osemkowe.append(i.strip())


def dziesiatkowe(num):
    return int(num, 8)


decymalne = []
for i in range(len(osemkowe)):
    decymalne.append(dziesiatkowe(osemkowe[i]))
counter = 0


for num in decymalne:
    num = str(num)
    if num[0] == num[-1]:
        counter += 1
print(counter)
