file = open("dane.txt", "r")
osemkowe = []

for i in file:
    osemkowe.append(i.strip())
counter = 0

for num in osemkowe:
    if num[0] == num[-1]:
        counter += 1

print(counter)
print(osemkowe)
