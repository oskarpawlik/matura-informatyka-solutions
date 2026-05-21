file = open("sygnaly.txt", "r")
slowa = []

for i in file:
    slowa.append(i.strip())

dlugosci = []

for i in slowa:
    dlugosci.append(len(set((i))))

maksymalna = max(dlugosci)
print(maksymalna)
print(slowa[dlugosci.index(maksymalna)])
