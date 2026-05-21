file = open("slowa.txt", "r")
slowa = []
for i in file:
    slowa.append(i.strip())


def najdl_blok(slowo):
    max_dlugosc = 1
    dlugosc = 1
    for i in range(len(slowo) - 1):
        if slowo[i] == slowo[i + 1] == "0":
            dlugosc += 1
            if dlugosc > max_dlugosc:
                max_dlugosc = dlugosc
        else:
            dlugosc = 1
    return max_dlugosc


maksymalna = 0

for i in slowa:
    if najdl_blok(i) > maksymalna:
        maksymalna = najdl_blok(i)
counter = 0
print(maksymalna)
for i in slowa:
    if najdl_blok(i) == maksymalna:
        print(i)
        counter += 1
