file = open("napisy.txt", "r")
napisy = []
for i in file:
    napisy.append(i.strip())


def grupowanie(napis):
    nowy = ""
    for i in range(len(napis) - 1):
        if napis[i].isdigit() and napis[i + 1].isdigit():
            litera = int(napis[i] + napis[i + 1])
            if 65 <= litera <= 90:
                nowy += chr(litera)
    return nowy


napis = ""
for i in napisy:
    napis += grupowanie(i)
for i in range(len(napis) - 2):
    if napis[i] == napis[i + 1] == napis[i + 2] == "X":
        print(napis[: i + 3])
        break
