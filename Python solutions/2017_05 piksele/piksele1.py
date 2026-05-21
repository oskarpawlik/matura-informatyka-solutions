file = open("przyklad.txt", "r")
data = []
for i in file:
    data.append(i.strip().split())
piksele = []
for i in data:
    for j in i:
        piksele.append(int(j))
print("najjaśniejszy", min(piksele))
print("najciemniejszy", max(piksele))
