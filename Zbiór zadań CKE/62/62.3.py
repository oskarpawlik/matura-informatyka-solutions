file1 = open("liczby1.txt", "r")
liczby1_oct = []
for line in file1:
    liczby1_oct.append(line.strip())
liczby1 = []
for i in range(len(liczby1_oct)):
    liczby1.append(int(liczby1_oct[i], 8))

file = open("liczby2.txt", "r")
liczby2 = []
for line in file:
    liczby2.append(int(line.strip()))
same_count = 0
for i in range(len(liczby1)):
    if liczby1[i] == liczby2[i]:
        same_count += 1
print("takie same:", same_count)
greater_count = 0
for i in range(len(liczby1)):
    if liczby1[i] > liczby2[i]:
        greater_count += 1
print("większe:", greater_count)
