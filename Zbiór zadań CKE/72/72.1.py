file = open("napisy.txt", "r")
napisy = []
for i in file:
    napisy.append(i.strip().split())


res = []
for para in napisy:
    if len(para[0]) >= 3 * len(para[1]) or len(para[1]) >= 3 * len(para[0]):
        res.append(1)
    else:
        res.append(0)
print(sum(res))
print(napisy[res.index(1)])
