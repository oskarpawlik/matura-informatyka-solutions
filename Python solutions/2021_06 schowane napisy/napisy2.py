file = open("napisy.txt", "r")
napisy = []
for i in file:
    napisy.append(i.strip())

haslo = ""
pozycja = 0
for i in range(19, len(napisy), 20):
    haslo += napisy[i][pozycja]
    pozycja += 1
print(haslo)
