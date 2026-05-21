file = open("galerie.txt", "r")
galerie = []
for i in file:
    galerie.append(i.strip().split())

rodzaje_lokali = []


def rodzaje(lokal):
    ilosc = []
    for i in range(2, len(lokal) - 1, 2):
        if (
            int(lokal[i]) * int(lokal[i + 1]) not in ilosc
            and int(lokal[i]) * int(lokal[i + 1]) != 0
        ):
            ilosc.append(int(lokal[i]) * int(lokal[i + 1]))
    return len(ilosc)


for galeria in galerie:
    rodzaje_lokali.append(rodzaje(galeria))

maksymalna = max(rodzaje_lokali)
minimalna = min(rodzaje_lokali)

print(galerie[rodzaje_lokali.index(minimalna)][1], minimalna)
print(galerie[rodzaje_lokali.index(maksymalna)][1], maksymalna)
