file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(int(i))


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


rozklady = []
counter = 0

for liczba in liczby:
    for i in range(1, liczba // 2 + 1):
        if is_prime(i) and is_prime(liczba - i):
            counter += 1
    rozklady.append(counter)
    counter = 0

minimum = min(rozklady)
minimum_index = rozklady.index(minimum)
maximum = max(rozklady)
maximum_index = rozklady.index(maximum)
print(liczby[maximum_index], maximum, liczby[minimum_index], minimum)
