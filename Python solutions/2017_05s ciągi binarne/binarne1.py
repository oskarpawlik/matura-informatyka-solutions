file = open("binarne.txt", "r")

ciagi = []
for i in file:
    ciagi.append(i.strip())


def dwucykliczny(napis):
    n = len(napis)
    if n % 2 != 0:
        return False
    if napis[0 : n // 2] == napis[n // 2 :]:
        return True
    return False


counter = 0
najdluzszy = ""
dlugosc = 0
for i in ciagi:
    if dwucykliczny(i):
        counter += 1
        if len(i) > dlugosc:
            najdluzszy = i
            dlugosc = len(i)
print(counter, najdluzszy, dlugosc)
