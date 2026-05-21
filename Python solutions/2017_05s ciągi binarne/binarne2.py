import math

file = open("binarne.txt", "r")

ciagi = []
for i in file:
    ciagi.append(i.strip())


def sprawdzenie(napis):
    for i in range(0, len(napis), 4):
        if int(napis[i : i + 4], 2) > 9:
            return True
    return False


dl = math.inf
counter = 0
for i in ciagi:
    if sprawdzenie(i):
        counter += 1
        if dl > len(i):
            dl = len(i)
print(counter, dl)
