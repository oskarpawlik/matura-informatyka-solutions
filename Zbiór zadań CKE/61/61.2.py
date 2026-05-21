file = open("ciagi.txt", "r")
ciagi_str = []
for i in file:
    if len(i.strip().split()) == 1:
        continue
    else:
        ciagi_str.append(i.strip().split())
ciagi = [[int(j) for j in i] for i in ciagi_str]

szesciany = [1]
i = 2
while szesciany[-1] < 1000000:
    szesciany.append(i**3)
    i += 1


def najw_szescian(arr, szesciany):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] in szesciany:
            return arr[i]
    return False


odp = []

for arr in ciagi:
    if najw_szescian(arr, szesciany) != False:
        odp.append(najw_szescian(arr, szesciany))
for i in odp:
    print(i)
