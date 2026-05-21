file = open("mecz.txt", "r")
dane = file.read().strip()


def passa(wyniki):
    dl = 1
    max_dl = 0
    ilosc = 0
    A_passy = []
    B_passy = []
    for i in range(len(wyniki) - 1):
        if wyniki[i] != wyniki[i + 1]:
            if wyniki[i] == "A" and dl >= 10:
                A_passy.append(dl)
                ilosc += 1
            elif wyniki[i] == "B" and dl >= 10:
                B_passy.append(dl)
                ilosc += 1
            if dl > max_dl:
                max_dl = dl
            dl = 0
        dl += 1
    if max_dl in A_passy:
        return ilosc, "A", max_dl
    return ilosc, "B", max_dl


print(passa(dane))
