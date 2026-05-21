file = open("liczby.txt", "r")
liczby_binarne = []
for i in file:
    liczby_binarne.append(i.strip())


def more_0_than_1(n):
    n = str(n)
    zera = n.count("0")
    jedynki = n.count("1")
    if zera > jedynki:
        return True
    return False


counter = 0
for i in liczby_binarne:
    if more_0_than_1(i):
        counter += 1
print(counter)
