file = open("dane_ulamki.txt", "r")
ulamki = []
for i in file:
    ulamki.append(i.split())
for i in range(len(ulamki)):
    ulamki[i][0] = int(ulamki[i][0])
    ulamki[i][1] = int(ulamki[i][1])


def czynnkiki(n):
    czynnki = []
    i = 2
    while n != 1:
        if n % i == 0:
            czynnki.append(i)
            n = n // i
            i = 1
        i += 1
    return set(czynnki)


def czy_nieskracalne(czynniki1, czynniki2):
    for i in czynniki1:
        for j in czynniki2:
            if i == j:
                return False
    return True


counter = 0
for ulamek in ulamki:
    if czy_nieskracalne(czynnkiki(ulamek[0]), czynnkiki(ulamek[1])):
        counter += 1
print(counter)
