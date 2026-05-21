import math

file = open("dron.txt", "r")
wsp = []
for line in file:
    para = [int(x) for x in line.split()]
    wsp.append(para)


counter = 0
for para in wsp:
    if math.gcd(para[0], para[1]) > 1:
        counter += 1
print(counter)
