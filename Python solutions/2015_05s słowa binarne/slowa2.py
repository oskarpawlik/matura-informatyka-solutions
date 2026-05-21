file = open("slowa.txt", "r")
slowa = []
for i in file:
    slowa.append(i.strip())


def bloki(slowo):
    bloki = 1
    for i in range(len(slowo) - 1):
        if slowo[i] != slowo[i + 1]:
            bloki += 1
    if bloki == 2 and slowo[0] == "0":
        return True
    return False


counter = 0
for i in slowa:
    if bloki(i):
        counter += 1
print(counter)
