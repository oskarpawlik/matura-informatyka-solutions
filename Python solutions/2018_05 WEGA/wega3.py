file = open("sygnaly.txt", "r")
slowa = []

for i in file:
    slowa.append(i.strip())


def warunek(slowo):
    ascii_slowa = []
    for i in slowo:
        ascii_slowa.append(ord(i))
    if max(ascii_slowa) - min(ascii_slowa) < 11:
        return True
    return False


for i in slowa:
    if warunek(i):
        print(i)
