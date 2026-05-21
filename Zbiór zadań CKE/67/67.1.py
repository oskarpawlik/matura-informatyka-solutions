def fib_list(n):
    fib = [1, 1]
    for i in range(1, n - 1):
        fib.append(fib[i] + fib[i - 1])
    return fib


def fib_wartosci(n):
    fib = [1, 1]
    for i in range(1, n - 1):
        fib.append(fib[i] + fib[i - 1])
    return fib[n - 1]


print("F10", fib_wartosci(10))
print("F20", fib_wartosci(20))
print("F20", fib_wartosci(30))
print("F30", fib_wartosci(40))
