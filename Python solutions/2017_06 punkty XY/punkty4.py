file = open("punkty.txt", "r")
punkty = []
for i in file:
    punkty.append(i.strip().split())
for i in range(len(punkty)):
    punkty[i] = list(map(int, punkty[i]))


def na_boku(x, y):
    if abs(x) == 5000 or abs(y) == 5000:
        return True
    return False


def w_srodku(x, y):
    if abs(x) < 5000 and abs(y) < 5000:
        return True
    return False


def na_zewnatrz(x, y):
    if abs(x) > 5000 or abs(y) > 5000:
        return True
    return False


wewnatrz = 0
zewnatrz = 0
bok = 0
for punkt in punkty:
    if na_zewnatrz(punkt[0], punkt[1]):
        zewnatrz += 1
    elif w_srodku(punkt[0], punkt[1]):
        wewnatrz += 1
    elif na_boku(punkt[0], punkt[1]):
        bok += 1
print(zewnatrz, wewnatrz, bok)
