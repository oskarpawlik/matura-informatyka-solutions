file1 = open("dane_systemy1.txt", "r")
file2 = open("dane_systemy2.txt", "r")
file3 = open("dane_systemy3.txt", "r")
S1 = []
S2 = []
S3 = []

for i in file1:
    S1.append(i.strip().split())
for i in file2:
    S2.append(i.strip().split())
for i in file3:
    S3.append(i.strip().split())
S1_dec_temp = []
S2_dec_temp = []
S3_dec_temp = []
for i in range(len(S1)):
    S1_dec_temp.append(int(S1[i][1], 2))
for i in range(len(S2)):
    S2_dec_temp.append(int(S2[i][1], 4))
for i in range(len(S3)):
    S3_dec_temp.append(int(S3[i][1], 8))

print("-" + bin(min(S1_dec_temp))[3::])
print("-" + bin(min(S2_dec_temp))[3::])
print("-" + bin(min(S3_dec_temp))[3::])
