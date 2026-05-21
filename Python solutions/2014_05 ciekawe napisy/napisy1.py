import math

file = open("NAPIS.TXT", "r")
data = []
for i in file:
    data.append(i.strip())


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


kody_ascii = []
for i in data:
    sum = 0
    for j in i:
        sum += ord(j)
    kody_ascii.append(sum)
counter = 0

for i in kody_ascii:
    if is_prime(i):
        counter += 1
print(counter)
