import math

file = open("dane4.txt", "r")
ciag = []
for i in file:
    ciag.append(i.strip())


def najw_luka(ciag):
    luka = 0
    for i in range(len(ciag) - 1):
        if abs(int(ciag[i]) - int(ciag[i + 1])) > luka:
            luka = abs(int(ciag[i]) - int(ciag[i + 1]))
    return luka


def najm_luka(ciag):
    luka = math.inf
    for i in range(len(ciag) - 1):
        if abs(int(ciag[i]) - int(ciag[i + 1])) < luka:
            luka = abs(int(ciag[i]) - int(ciag[i + 1]))
    return luka


najw_luki = []
najm_luki = []

for i in ciag:
    najw_luki.append(najw_luka(ciag))
    najm_luki.append(najm_luka(ciag))
print(max(najw_luki))
print(min(najm_luki))
