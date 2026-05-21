file = open("pi.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())
counter = 0
for i in range(len(liczby) - 1):
    if int(liczby[i] + liczby[i + 1]) > 90:
        counter += 1
print(counter)
