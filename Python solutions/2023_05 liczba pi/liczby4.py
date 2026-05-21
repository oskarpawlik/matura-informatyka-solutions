file = open("pi.txt", "r")
liczby = []
for i in file:
    liczby.append(int(i))

counter = 0
ciagi = []
for i in range(0, len(liczby) - 5):
    czy_M = True
    czy_R = True
    poprzednia_liczba = liczby[i]

    for j in range(1, 6):
        obecna_liczba = liczby[i + j]
        if czy_R and poprzednia_liczba >= obecna_liczba:
            czy_R = False
        elif not czy_R and czy_M and obecna_liczba >= poprzednia_liczba:
            czy_M = False
            break
        poprzednia_liczba = obecna_liczba
    if czy_R == False and czy_M == True:
        czy_maleje_conajmniej_raz = False
        ciag = liczby[i : i + 6]

        for k in range(len(ciag) - 1):
            if ciag[k + 1] < ciag[k]:
                czy_maleje_conajmniej_raz = True
        if czy_maleje_conajmniej_raz:
            counter += 1
            ciagi.append(liczby[i : i + 6])

print(counter)
print(ciagi)
