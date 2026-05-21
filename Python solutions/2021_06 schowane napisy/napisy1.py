file = open("napisy.txt", "r")
napisy = []
for i in file:
    napisy.append(i.strip())

suma = 0
for napis in napisy:
    for i in napis:
        if i.isdigit():
            suma += 1
print(suma)
