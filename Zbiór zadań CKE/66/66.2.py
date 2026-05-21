file = open("trojki.txt", "r")
trojki = []
for line in file:
    trojki.append(line.strip().split())
for i in range(len(trojki)):
    trojki[i] = list(map(int, trojki[i]))


def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def warunek(l1, l2, l3):
    if is_prime(l1) and is_prime(l2) and l1 * l2 == l3:
        return True
    return False


for i in trojki:
    if warunek(i[0], i[1], i[2]):
        print(i)
