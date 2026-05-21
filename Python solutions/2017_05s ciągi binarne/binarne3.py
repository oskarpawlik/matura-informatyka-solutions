file = open("binarne.txt", "r")

ciagi = []
for i in file:
    ciagi.append(i.strip())
liczby = []

for i in ciagi:
    liczba = int(i, 2)
    if liczba < 65535:
        liczby.append(liczba)

print(max(liczby), bin(max(liczby))[2:])
