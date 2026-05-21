file = open("sygnaly.txt", "r")
slowa = []

for i in file:
    slowa.append(i.strip())
slowo = ""
for i in range(39, len(slowa), 40):
    slowo += slowa[i][9]
print(slowo)
