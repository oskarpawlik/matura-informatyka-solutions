file = open("anagram.txt", "r")
data = []
for i in file:
    data.append(i.strip().split())
wynik = []

for i in data:
    if len(i[0]) == len(i[1]) == len(i[2]) == len(i[3]) == len(i[4]):
        wynik.append(i)
for i in wynik:
    print(i)

print(len(wynik))
