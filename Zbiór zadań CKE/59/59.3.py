file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(int(i.strip()))


def iloczyn(n):
    iloczyn = 1
    for i in str(n):
        iloczyn *= int(i)
    return iloczyn


def moc(n):
    moc = 1
    liczba = iloczyn(n)
    while liczba > 9:
        liczba = iloczyn(liczba)
        moc += 1
    return moc


moce = []
for i in liczby:
    moce.append(moc(i))
print("moc 1:", moce.count(1))
print("moc 2:", moce.count(2))
print("moc 3:", moce.count(3))
print("moc 4:", moce.count(4))
print("moc 5:", moce.count(5))
print("moc 6:", moce.count(6))
print("moc 7:", moce.count(7))
print("moc 8:", moce.count(8))

minimalna = 99999999
maksymalna = 0
for i in range(len(liczby)):
    if maksymalna < liczby[i] and moce[i] == 1:
        maksymalna = liczby[i]
    if minimalna > liczby[i] and moce[i] == 1:
        minimalna = liczby[i]
print("maksymalna:", maksymalna)
print("minimalna:", minimalna)
