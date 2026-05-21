file = open("punkty.txt", "r")
punkty = []
for i in file:
    punkty.append(i.strip().split())


def cyfro_podobne(X, Y):
    if set(X) == set(Y):
        return True
    return False


counter = 0
for punkt in punkty:
    if cyfro_podobne(punkt[0], punkt[1]):
        counter += 1
print(counter)
