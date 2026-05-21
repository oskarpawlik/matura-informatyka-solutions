file = open("anagram.txt", "r")
data = []
for i in file:
    data.append(i.strip().split())
posortowane = []
temp = []
for line in data:
    for i in line:
        temp.append(sorted(i))
    posortowane.append(temp)
    temp = []
czy_anagram = []
for i in posortowane:
    if i[0] == i[1] == i[2] == i[3] == i[4]:
        czy_anagram.append(1)
    else:
        czy_anagram.append(0)

for i in range(len(czy_anagram)):
    if czy_anagram[i] == 1:
        print(data[i])
