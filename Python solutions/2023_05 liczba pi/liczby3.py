file = open("pi.txt", "r")
liczby = []
for i in file:
    liczby.append(int(i))


def rosnaco_malejacy(c):
    if (c[0] < c[1]) and (c[2] > c[3] > c[4] > c[5]):
        return True
    if (c[0] < c[1] < c[2]) and (c[3] > c[4] > c[5]):
        return True
    if (c[0] < c[1] < c[2] < c[3]) and (c[4] > c[5]):
        return True
    return False


counter = 0
for i in range(len(liczby) - 5):
    if rosnaco_malejacy(liczby[i : i + 6]):
        counter += 1

print(counter)
