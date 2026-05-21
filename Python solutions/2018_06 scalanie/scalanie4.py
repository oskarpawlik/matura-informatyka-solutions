file1 = open("dane1.txt", "r")
file2 = open("dane2.txt", "r")
dane1 = []
dane2 = []
for i in file1:
    dane1.append(i.strip().split())
for i in file2:
    dane2.append(i.strip().split())
for i in range(len(dane1)):
    dane1[i] = list(map(int, dane1[i]))
for i in range(len(dane2)):
    dane2[i] = list(map(int, dane2[i]))


def scalanie(ciag1, ciag2):
    nowy = []
    pierwszy = 0
    drugi = 0
    while pierwszy < 10 and drugi < 10:
        if ciag1[pierwszy] <= ciag2[drugi]:
            nowy.append(ciag1[pierwszy])
            pierwszy += 1
        else:
            nowy.append(ciag2[drugi])
            drugi += 1
    if pierwszy != 10:
        for i in range(pierwszy, len(ciag1)):
            nowy.append(ciag1[i])
    else:
        for i in range(drugi, len(ciag2)):
            nowy.append(ciag2[i])
    return nowy


for i in range(len(dane1)):
    print(scalanie(dane1[i], dane2[i]))
