file = open("dane.txt", "r")
data = []
for i in file:
    data.append(i.strip().split())
kontrastujace = []
for i in range(200):
    kontrastujace.append([0] * 320)

for line in range(200):
    for row in range(320 - 1):
        if abs(int(data[line][row]) - int(data[line][row + 1])) > 128:
            kontrastujace[line][row] = 1
            kontrastujace[line][row + 1] = 1
for rows in range(320):
    for line in range(200 - 1):
        if abs(int(data[line][rows]) - int(data[line + 1][rows])) > 128:
            kontrastujace[line][rows] = 1
            kontrastujace[line + 1][rows] = 1
counter = 0
for i in kontrastujace:
    for j in i:
        if j == 1:
            counter += 1
print(counter)
