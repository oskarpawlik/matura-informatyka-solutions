file = open("slowa.txt", "r")
slowa = []
for i in file:
    slowa.append(i.strip())


def czy_wieksza(slowo):
    zera = slowo.count("0")
    jedynki = slowo.count("1")
    if zera > jedynki:
        return True
    return False


counter = 0
for i in slowa:
    if czy_wieksza(i):
        counter += 1
print(counter)
