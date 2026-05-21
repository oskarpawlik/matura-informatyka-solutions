file = open("liczby2.txt", "r")
liczby = []
for line in file:
    liczby.append(int(line.strip()))
ciag = [1] * len(liczby)
print(liczby)
for i in range(len(liczby) - 1):
    if liczby[i] <= liczby[i + 1]:
        ciag[i + 1] = ciag[i] + 1
max_ciagu = max(ciag)
print(liczby[ciag.index(max_ciagu) - max_ciagu + 1])
print("elementy", max_ciagu)
