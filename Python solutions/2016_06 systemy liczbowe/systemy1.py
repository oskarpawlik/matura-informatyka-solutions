file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())


def oct(n):
    if n[-1] == "8":
        return True
    return False


counter = 0
for i in liczby:
    if oct(i):
        counter += 1
print(counter)
