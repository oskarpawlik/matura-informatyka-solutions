file = open("instrukcje.txt", "r")
instrukcje = []
for i in file:
    instrukcje.append(i.strip().split())
ciag = [1] * len(instrukcje)
for i in range(len(instrukcje) - 1):
    if instrukcje[i][0] == instrukcje[i + 1][0]:
        ciag[i + 1] = ciag[i] + 1
najdluzszy = max(ciag)
print(najdluzszy)
print(instrukcje[ciag.index(najdluzszy)][0])
