from collections import Counter

file = open("dane.txt", "r")
ciag = []
for line in file:
    for i in line:
        ciag.append(i)
liczby = []

cyfry = ""
for i in range(len(ciag)):
    if ciag[i].isdigit():
        cyfry += ciag[i]

res = Counter(cyfry)
print(res)
