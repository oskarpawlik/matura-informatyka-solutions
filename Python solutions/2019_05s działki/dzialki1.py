file = open("dzialki.txt", "r")
dzialki = []
dzialka = []
for line in file:
    if line != "\n":
        dzialka.append(line.strip())
    else:
        dzialki.append(dzialka)
        dzialka = []


def trawa(dzialka):
    counter = 0
    for i in dzialka:
        counter += i.count("*")
    if counter / (30 * 30) >= 0.7:
        return True
    return False


couter = 0
for dzialka in dzialki:
    if trawa(dzialka):
        couter += 1
print(couter)
