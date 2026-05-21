file = open("liczby.txt", "r")
data = []
for i in file:
    data.append(i.strip())
dec = []

for i in data:
    dec.append(int(i, 2))

counter = 0
for i in dec:
    if i % 2 == 0:
        counter += 1
print(counter)

maksymalna = max(dec)
print(maksymalna)
print(bin(maksymalna)[2::])

sum = 0
count = 0
for i in range(len(data)):
    if len(data[i]) == 9:
        count += 1
        sum += dec[i]
print(count, bin(sum)[2::])
