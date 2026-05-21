file = open("hasla.txt", "r")
hasla = []
for i in file:
    hasla.append(i.strip())


def numeric_pass(haslo):
    for i in haslo:
        if not i.isdigit():
            return False
    return True


counter = 0
for haslo in hasla:
    if numeric_pass(haslo):
        counter += 1
print(counter)
