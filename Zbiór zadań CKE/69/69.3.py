file = open("dane_geny.txt", "r")
genotypy = []
for i in file:
    genotypy.append(i.strip())


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

    return geny


geny_lista = []
for i in genotypy:
    for j in geny(i):
        geny_lista.append(j)
dlugosci = []
for i in geny_lista:
    dlugosci.append(len(i))
print("najdluzszy gen", max(dlugosci))

osobniki = []
for i in genotypy:
    osobniki.append(geny(i))
najw_liczba = 0

for i in osobniki:
    if najw_liczba < len(set(i)):
        najw_liczba = len(i)
print("najwieksza liczba genow w genotypie", najw_liczba)
