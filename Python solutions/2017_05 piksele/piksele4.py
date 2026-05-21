from sys import orig_argv

file = open("dane.txt", "r")
data = []
for i in file:
    data.append(i.strip().split())

ciag = []
for i in range(200):
    ciag.append([1] * 320)

counter = 1
for rows in range(320):
    for line in range(200 - 1):
        if data[line][rows] == data[line + 1][rows]:
            ciag[line + 1][rows] = counter + 1
            counter += 1
        else:
            counter = 1
            ciag[line + 1][rows] = counter + 1
razem = []
for i in ciag:
    for j in i:
        razem.append(j)
print(max(razem))
