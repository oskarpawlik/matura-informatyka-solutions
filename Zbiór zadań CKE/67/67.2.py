def fib_list(n):
    fib = [1, 1]
    for i in range(1, n - 1):
        fib.append(fib[i] + fib[i - 1])
    return fib


fibonacci = fib_list(40)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


for i in range(len(fibonacci)):
    if is_prime(fibonacci[i]):
        print(i + 1, fibonacci[i])
