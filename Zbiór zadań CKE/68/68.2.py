file = open("dane_napisy.txt", "r")
anagramy = []
for i in file:
    anagramy.append(i.strip().split())


def czy_anagram(napis1, napis2):
    if len(napis1) != len(napis2):
        return False
    litery1 = []
    litery2 = []
    for i in range(len(napis1)):
        litery1.append(napis1[i])
        litery2.append(napis2[i])
    litery1.sort()
    litery2.sort()
    if litery1 == litery2:
        return True
    return False


counter = 0
for i in anagramy:
    if czy_anagram(i[0], i[1]):
        counter += 1
print(counter)
