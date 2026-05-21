file = open("trojki.txt", "r")
trojki = []
for line in file:
    trojki.append(line.strip().split())


def warunek(l1, l2, l3):
    sum1 = 0
    sum2 = 0
    for i in l1:
        sum1 += int(i)
    for i in l2:
        sum2 += int(i)
    if sum1 + sum2 == int(l3):
        return True
    return False


for i in trojki:
    if warunek(i[0], i[1], i[2]):
        print(i)
