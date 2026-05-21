file = open("pary.txt", "r")
pary_temp = []
for i in file:
    pary_temp.append(i.strip().split())
pary = []
for para in pary_temp:
    if int(para[0]) == len(para[1]):
        pary.append([int(para[0]), para[1]])

najmniejsza = pary[0]
for para in pary:
    if para[0] < najmniejsza[0]:
        najmniejsza = para
    if para[0] == najmniejsza[0] and sorted(para[1]) < sorted(najmniejsza[1]):
        najmniejsza = para
print(najmniejsza)
