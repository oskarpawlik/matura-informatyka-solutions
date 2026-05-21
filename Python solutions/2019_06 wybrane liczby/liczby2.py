file = open("pierwsze.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())
liczby_rev = []
for i in liczby:
    liczby_rev.append(i[::-1])


def is_prime(n):
    n = int(n)
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


for i in range(len(liczby)):
    if is_prime(liczby[i]) and is_prime(liczby_rev[i]):
        print(liczby[i])
