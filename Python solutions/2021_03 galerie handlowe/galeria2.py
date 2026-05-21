file = open("galerie.txt", "r")
galerie = []
for i in file:
    galerie.append(i.strip().split())


def liczba_lokali(lokal):
    counter = 0
    for i in range(2, len(lokal) - 1, 2):
        if int(lokal[i]) == int(lokal[i + 1]) == 0:
            return counter
        else:
            counter += 1


def powierzchnia(lokal):
    powierzchnia = 0
    for i in range(2, len(lokal) - 1, 2):
        powierzchnia += int(lokal[i]) * int(lokal[i + 1])
    return powierzchnia


dane_b = []

for galeria in galerie:
    print(galeria[1], powierzchnia(galeria), liczba_lokali(galeria))
    dane_b.append([galeria[1], powierzchnia(galeria)])

max_pow = 0
min_pow = 10**100
max_miasto = ""
min_miasto = ""

for i in range(len(dane_b)):
    if dane_b[i][1] > max_pow:
        max_pow = dane_b[i][1]
        max_miasto = dane_b[i][0]
    if dane_b[i][1] < min_pow:
        min_pow = dane_b[i][1]
        min_miasto = dane_b[i][0]

print()
print(min_miasto, min_pow)
print(max_miasto, max_pow)


print()
# lepszy sposob
najnizszy = min(dane_b, key=lambda x: x[1])
najwyzszy = max(dane_b, key=lambda x: x[1])

print(f"Minimum: {najnizszy[0]} {najnizszy[1]}")
print(f"Maximum: {najwyzszy[0]} {najwyzszy[1]}")
