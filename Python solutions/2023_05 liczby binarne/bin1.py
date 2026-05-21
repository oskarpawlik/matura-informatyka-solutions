file = open("bin.txt", "r")
liczby = []
for line in file:
    liczby.append(line.strip())


def bloki(num):
    counter = 0
    for i in range(len(num) - 1):
        if num[i] != num[i + 1]:
            counter += 1
    if counter == 1 or counter == 0:
        return True
    return False


tmp = 0
for i in liczby:
    if bloki(i):
        tmp += 1
print(tmp)
