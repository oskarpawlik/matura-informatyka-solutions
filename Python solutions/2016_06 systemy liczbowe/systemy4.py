file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())


def oct(n):
    liczba = n[0 : len(n) - 1]
    system = int(n[-1])
    if system == 8:
        return int(liczba, 8)
    return 0


suma = 0
for i in liczby:
    suma += oct(i)
print(suma)
