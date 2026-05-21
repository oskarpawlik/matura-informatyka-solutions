file = open("dane_geny.txt", "r")
genotypy = []
for i in file:
    genotypy.append(i.strip())


def geny(genotyp):
    marker = []
    for i in range(len(genotyp) - 1):
        if genotyp[i] == genotyp[i + 1] == "A":
            marker.append("A")
        elif genotyp[i] == genotyp[i + 1] == "B":
            marker.append("B")
        else:
            marker.append("0")

    gen = ""
    geny = []
    for j in range(len(marker) - 1):
        if marker[j] == "A":
            for k in range(j, len(marker)):
                gen += genotyp[k]
                if marker[k] == "B":
                    gen += "B"
                    geny.append(gen)
                    break
        gen = ""
    return geny


geny_lista = []
for i in genotypy:
    for j in geny(i):
        geny_lista.append(j)

counter = 0
mutacje_lista = []
for i in genotypy:
    for j in geny(i):
        if "BCDDC" in j:
            counter += 1
            break

print(counter)
