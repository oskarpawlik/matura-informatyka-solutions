file = open("punkty.txt", "r")
punkty = []
for i in file:
    punkty.append(i.strip().split())
for i in range(len(punkty)):
    punkty[i] = list(map(int, punkty[i]))


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


counter = 0
for punkt in punkty:
    if is_prime(punkt[0]) and is_prime(punkt[1]):
        counter += 1
print(counter)
