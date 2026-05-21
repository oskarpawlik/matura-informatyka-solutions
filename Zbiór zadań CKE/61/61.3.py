file = open("bledne.txt", "r")
ciagi_str = []
for i in file:
    if len(i.strip().split()) == 1:
        continue
    else:
        ciagi_str.append(i.strip().split())
ciagi = [[int(j) for j in i] for i in ciagi_str]
print(ciagi)


def find_error(arr):
    roznice = []
    for i in range(len(arr) - 1):
        roznice.append(arr[i + 1] - arr[i])

    r = max(set(roznice), key=roznice.count)
    # sprawdzamy czy pierwszy jest okej
    if arr[1] + r == arr[2]:
        if arr[0] + r != arr[1]:
            return arr[0]
    # sprawdzenie czy każdy następny nie jest zly przypadkiem
    for i in range(len(arr) - 1):
        if arr[i] + r != arr[i + 1]:
            return arr[i + 1]


for i in ciagi:
    print(find_error(i))
