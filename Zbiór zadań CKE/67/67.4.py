def fib_list(n):
    fib = [1, 1]
    for i in range(1, n - 1):
        fib.append(fib[i] + fib[i - 1])
    return fib


fibonacci = fib_list(40)
fib_bin = []

for i in fibonacci:
    fib_bin.append(bin(i)[2::])
for i in fib_bin:
    if i.count("1") == 6:
        print(i)
