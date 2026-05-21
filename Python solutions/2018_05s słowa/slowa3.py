file = open("slowa.txt", "r")
slowa = []
for i in file:
    slowa.append(i.strip().split())

counter = 0
for para in slowa:
    if sorted(para[0]) == sorted(para[1]):
        counter += 1
print(counter)
