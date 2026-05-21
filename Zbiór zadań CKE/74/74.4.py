file = open("hasla.txt", "r")
hasla = []
for i in file:
    hasla.append(i.strip())


def warunek(haslo):
    upper = False
    lower = False
    number = False
    for i in haslo:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            number = True
    if upper and lower and number:
        return True
    return False


counter = 0
for i in hasla:
    if warunek(i):
        counter += 1
print(counter)
