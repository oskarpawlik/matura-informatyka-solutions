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


counter = 0
for i in liczby:
    if is_prime(i - 1):
        counter += 1

print(counter)
