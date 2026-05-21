file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(int(i.strip()))


def czynniki_pierwsze(n):
    czynnik = 3
    ile = 0
    if n % 2 == 0:
        return False
    while n > 1:
        if n % czynnik == 0:
            ile += 1
        while n % czynnik == 0:
            n /= czynnik
        czynnik += 2
        if ile > 3:
            return False
    if ile == 3:
        return True
    else:
        return False


counter = 0
for i in liczby:
    if czynniki_pierwsze(i):
        counter += 1
print(counter)
