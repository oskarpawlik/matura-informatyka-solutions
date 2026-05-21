file = open("NAPIS.TXT", "r")
data = []

for i in file:
    data.append(i.strip())
same = []

for i in data:
    if data.count(i) > 1:
        same.append(i)
same = set(same)
print(same)
