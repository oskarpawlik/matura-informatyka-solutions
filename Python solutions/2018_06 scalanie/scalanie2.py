file1 = open("dane1.txt", "r")
file2 = open("dane2.txt", "r")
dane1 = []
dane2 = []
for i in file1:
    dane1.append(i.strip().split())
for i in file2:
    dane2.append(i.strip().split())
for i in range(len(dane1)):
    dane1[i] = list(map(int, dane1[i]))
for i in range(len(dane2)):
    dane2[i] = list(map(int, dane2[i]))


def warunek(ciag1, ciag2):
    counter1 = 0
    counter2 = 0
    for i in range(len(ciag1)):
        if ciag1[i] % 2 == 1:
            counter1 += 1
        if ciag2[i] % 2 == 1:
            counter2 += 1
    if counter1 == counter2 == 5:
        return True
    return False


counter = 0
for i in range(len(dane1)):
    if warunek(dane1[i], dane2[i]):
        counter += 1
print(counter)
