file = open("dane.txt", "r")
data = []
for i in file:
    data.append(i.strip().split())


def czy_symetryczny(wiersz):
    for i in range(int(len(wiersz) / 2)):
        if wiersz[i] != wiersz[len(wiersz) - 1 - i]:
            return False
    return True


counter = 0
for i in data:
    if czy_symetryczny(i) == False:
        counter += 1
print(counter)
