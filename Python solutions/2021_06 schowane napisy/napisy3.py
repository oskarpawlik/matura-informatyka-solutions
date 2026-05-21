file = open("napisy.txt", "r")
napisy = []
for i in file:
    napisy.append(i.strip())


def tworzenie(napis):
    pierwsza_odcieta = napis[1::]
    ostatnia_odcieta = napis[0 : len(napis) - 1]
    if pierwsza_odcieta == pierwsza_odcieta[::-1]:
        return pierwsza_odcieta[24]
    elif ostatnia_odcieta == ostatnia_odcieta[::-1]:
        return ostatnia_odcieta[24]
    return False


haslo = ""
for i in napisy:
    if tworzenie(i):
        haslo += tworzenie(i)
print(haslo)
