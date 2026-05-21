file = open("hasla.txt", "r")
hasla = []
for i in file:
    hasla.append(i.strip())
takie_same = []
for i in range(len(hasla)):
    for j in range(1 + i, len(hasla)):
        if hasla[i] == hasla[j]:
            takie_same.append(hasla[i])
takie_same.sort()
for i in takie_same:
    print(i)
