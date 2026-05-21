import math

file1 = open("dane_systemy1.txt", "r")
S1 = []
for i in file1:
    S1.append(i.strip().split())
S1_dec_temp = []
for i in range(len(S1)):
    S1_dec_temp.append(int(S1[i][1], 2))


def step(i, j, ti, tj):
    r = pow(ti - tj, 2)
    if j == i:
        return 0
    return math.ceil(r / abs(i - j))


steps = []
for i in range(len(S1_dec_temp)):
    for j in range(len(S1_dec_temp)):
        steps.append(step(i + 1, j + 1, S1_dec_temp[i], S1_dec_temp[j]))
print(max(steps))
