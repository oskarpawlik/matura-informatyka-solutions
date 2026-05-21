file = open("dane_geny.txt", "r")
genotypy = []
for i in file:
    genotypy.append(i.strip())


def is_palindrome(genotyp):
    if genotyp == genotyp[::-1]:
        return True
    return False


silnie_odporne = 0
for i in genotypy:
    if is_palindrome(i):
        silnie_odporne += 1
print("silnie odporne", silnie_odporne)


def geny(genotyp):
    marker = []
    for i in range(len(genotyp) - 1):
        if genotyp[i] == "A" and genotyp[i + 1] == "A":
            marker.append("START")
        elif genotyp[i] == "B" and genotyp[i + 1] == "B":
            marker.append("KONIEC")
        else:
            marker.append("0")

    gen = ""
    geny = []
    budowanie = False
    for i in range(len(marker)):
        if marker[i] == "START":
            budowanie = True
        if budowanie:
            gen += genotyp[i]
        if marker[i] == "KONIEC" and budowanie == True:
            budowanie = False
            gen += "B"
            geny.append(gen)
            gen = ""
    return sorted(geny)


counter = 0
for i in genotypy:
    if geny(i) == geny(i[::-1]):
        counter += 1

print(counter)
