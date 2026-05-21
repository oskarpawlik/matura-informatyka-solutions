file = open("slowa.txt", "r")
slowa = []
for i in file:
    slowa.append(i.strip().split())

counter = 0
for para in slowa:
    if para[0] in para[1]:
        counter += 1
print(counter)
