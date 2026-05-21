file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())


def warunek(n):
    liczba = n[0 : len(n) - 1]
    system = int(n[-1])
    if system == 4 and "0" not in liczba:
        return True
    return False


counter = 0
for i in liczby:
    if warunek(i):
        counter += 1
print(counter)
