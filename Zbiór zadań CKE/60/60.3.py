file = open("liczby.txt", "r")
liczby = []
for line in file:
    liczby.append(int(line))
liczby.sort()

for i in range(len(liczby)):
    counter = 0
    for j in range(2, len(liczby)):
        if liczby[i] % j == 0:
            counter += 1
        if counter >= 2:
            liczby[i] = 1
print(max(liczby))
