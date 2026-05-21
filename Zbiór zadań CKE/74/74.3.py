file = open("hasla.txt", "r")
hasla = []
for i in file:
    hasla.append(i.strip())


def four_digits_ascii(napis):
    for i in range(len(napis) - 3):
        ascii_list = [
            ord(napis[i]),
            ord(napis[i + 1]),
            ord(napis[i + 2]),
            ord(napis[i + 3]),
        ]
        ascii_list.sort()
        if ascii_list[0] == ascii_list[1] - 1 == ascii_list[2] - 2 == ascii_list[3] - 3:
            return True
    return False


counter = 0
for i in hasla:
    if four_digits_ascii(i):
        counter += 1
print(counter)
