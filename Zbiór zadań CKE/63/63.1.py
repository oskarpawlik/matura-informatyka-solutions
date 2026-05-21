file = open("ciagi.txt", "r")
ciagi = []
for i in file:
    ciagi.append(i.strip())
print(ciagi)


def czy_dwucykliczny(n):
    dl = len(n)
    if dl % 2 != 0:
        return False
    elif n[0 : dl // 2] == n[dl // 2 :]:
        return True
    return False


for i in ciagi:
    if czy_dwucykliczny(i):
        print(i)
