file = open("dane_napisy.txt", "r")
anagramy = []
for i in file:
    anagramy.append(i.strip().split())


def czy_jednolity(napis1, napis2):
    if napis1 == napis2:
        return True
    return False


counter = 0
for i in anagramy:
    if czy_jednolity(i[0], i[1]):
        counter += 1
print(counter)
