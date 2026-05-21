file = open("instrukcje.txt", "r")
instrukcje = []

for i in file:
    instrukcje.append(i.strip().split())
dict = {}

for i in range(len(instrukcje)):
    if instrukcje[i][0] == "DOPISZ":
        if instrukcje[i][1] not in dict:
            dict[instrukcje[i][1]] = 1
        else:
            dict[instrukcje[i][1]] += 1
maksymalna = max(dict.values())

for i in dict.keys():
    if dict[i] == maksymalna:
        print(i, dict[i])
