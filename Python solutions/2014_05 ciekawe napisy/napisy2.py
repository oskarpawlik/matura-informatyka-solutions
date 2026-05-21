file = open("NAPIS.TXT", "r")
data = []
for i in file:
    data.append(i.strip())


def is_growing(name):
    for i in range(len(name) - 1):
        if ord(name[i]) >= ord(name[i + 1]):
            return False
    return True


growing = []

for i in data:
    if is_growing(i):
        growing.append(i)
print(growing)
