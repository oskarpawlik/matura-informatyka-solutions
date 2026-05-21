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
counter = 0

for i in range(len(dane1)):
    if dane1[i][-1] == dane2[i][-1]:
        counter += 1
print(counter)
