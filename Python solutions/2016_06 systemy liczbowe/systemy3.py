file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())


def parzyste(n):
    liczba = n[0 : len(n) - 1]
    system = int(n[-1])
    if system != 2:
        return False
    if int(liczba, 2) % 2 == 0:
        return True
    return False


counter = 0
for i in liczby:
    if parzyste(i):
        counter += 1
print(counter)
