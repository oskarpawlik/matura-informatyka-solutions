file = open("napisy.txt", "r")
napisy = []
for i in file:
    napisy.append(i.strip().split())


def otrzymanie(napis1, napis2):
    if len(napis1) >= len(napis2):
        return False
    if napis1 == napis2[0 : len(napis1)]:
        return napis1, napis2, napis2[len(napis1) : :]
    return False


for napis in napisy:
    if otrzymanie(napis[0], napis[1]) != False:
        print(otrzymanie(napis[0], napis[1]))
