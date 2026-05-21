with open("pi.txt") as f:
    s = "".join(line.strip() for line in f)

best_start = 0
best_len = 0

for i in range(len(s)):
    j = i

    while j + 1 < len(s) and s[j] < s[j + 1]:
        j += 1

    # if j == i:
    #    continue

    while j + 1 < len(s) and s[j] > s[j + 1]:
        j += 1

    # if j == i:
    #    continue

    length = j - i + 1

    if length >= 4 and length > best_len:
        best_len = length
        best_start = i

print(best_start + 1)
print(s[best_start : best_start + best_len])
