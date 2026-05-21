file = open("ciagi.txt", "r")
ciagi = []
for i in file:
    ciagi.append(i.strip())


def warunek(n):
    for i in range(len(n) - 1):
        if n[i] == n[i + 1] == "1":
            return False
    return True


counter = 0

for i in ciagi:
    if warunek(i):
        counter += 1
print(counter)
