file = open("slowa.txt", "r")
slowa = []
for i in file:
    slowa.append(i.strip().split())


counter = 0
for para in slowa:
    for slowo in para:
        if slowo[-1] == "A":
            counter += 1
print(counter)
