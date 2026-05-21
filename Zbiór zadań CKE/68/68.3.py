file = open("dane_napisy.txt", "r")
anagramy = []

for i in file:
    anagramy.append(i.strip().split())
napisy = []

for para in anagramy:
    for i in para:
        napisy.append(i)
for i in range(len(napisy)):
    napisy[i] = ("").join(sorted(napisy[i]))
napisy_bez_powt = set(napisy)

k = []
temp = 0
for i in napisy_bez_powt:
    for j in napisy:
        if i == j:
            temp += 1
    k.append(temp)
    temp = 0
print(max(k))
