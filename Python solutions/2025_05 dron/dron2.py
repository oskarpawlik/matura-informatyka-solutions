file = open("dron.txt", "r")
wsp = []
for line in file:
    para = [int(x) for x in line.split()]
    wsp.append(para)

pozycje = [[0, 0]]
poz_x = 0
poz_y = 0
for para in wsp:
    poz_x += para[0]
    poz_y += para[1]
    pozycje.append([poz_x, poz_y])

counter = 0
for para in pozycje:
    if 0 < para[0] < 5000 and 0 < para[1] < 5000:
        counter += 1
print(counter)
