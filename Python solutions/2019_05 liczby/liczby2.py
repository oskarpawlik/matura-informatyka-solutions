file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())


def warunek(num):
    sum = 0
    for i in num:
        sum += factorial(int(i))
    if sum == int(num):
        return True
    return False


def factorial(num):
    result = 1
    if num == 0:
        return 1
    while num > 1:
        result *= num
        num -= 1
    return result


for i in liczby:
    if warunek(i):
        print(i)
