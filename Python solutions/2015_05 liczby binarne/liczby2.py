file = open("liczby.txt", "r")
liczby_binarne = []
for i in file:
    liczby_binarne.append(i.strip())


def by_two(n):
    if int(n) % 2 == 0:
        return True
    return False


def by_eight(n):
    if int(n) % 8 == 0:
        return True
    return False


count_two = 0
count_eight = 0
for i in liczby_binarne:
    if by_two(i):
        count_two += 1
    if by_eight(i):
        count_eight += 1
print(count_two)
print(count_eight)
