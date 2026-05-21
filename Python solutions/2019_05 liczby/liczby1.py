file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(int(i))


def is_hex_digit(num):
    if num == 1:
        return True
    while num != 1:
        if num % 3 == 0:
            num //= 3
        else:
            return False
    return True


counter = 0
for i in liczby:
    if is_hex_digit(i):
        counter += 1
print(counter)
