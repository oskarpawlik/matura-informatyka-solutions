file = open("tekst.txt", "r")

for i in file:
    slowa = i.strip().split(" ")


def dwie_kolejne(slowo):
    for i in range(len(slowo) - 1):
        if slowo[i] == slowo[i + 1]:
            return True
    return False


counter = 0
for slowo in slowa:
    if dwie_kolejne(slowo):
        counter += 1
print("slowa z dwoma kolejnymi", counter)
