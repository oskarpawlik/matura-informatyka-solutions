file = open("galerie.txt", "r")
galerie = []
for i in file:
    galerie.append(i.strip().split())
kraje = {}
for galeria in galerie:
    if galeria[0] not in kraje:
        kraje[galeria[0]] = 1
    else:
        kraje[galeria[0]] += 1
for i in kraje:
    print(i, kraje[i])
