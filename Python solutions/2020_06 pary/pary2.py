file = open("pary.txt", "r")
pary = []
for i in file:
    pary.append(i.strip().split())
slowa = []
for para in pary:
    slowa.append(para[1])


def najdl_ciag(slowo):
    ciag = [1] * len(slowo)
    for i in range(len(slowo) - 1):
        if slowo[i] == slowo[i + 1]:
            ciag[i + 1] = ciag[i] + 1
    return max(ciag) * slowo[ciag.index(max(ciag))], max(ciag)


for i in slowa:
    print(najdl_ciag(i))
