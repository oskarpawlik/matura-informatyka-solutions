file = open("pary.txt", "r")
pary = []
for i in file:
    pary.append(i.strip().split())

for para in pary:
    para[0] = int(para[0])


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


def para_pierszych(liczba):
    for i in range(1, liczba + 1):
        if is_prime(i) and is_prime(liczba - i):
            return i, liczba - i


for para in pary:
    if para[0] % 2 == 0:
        print(para[0], para_pierszych(para[0]))
