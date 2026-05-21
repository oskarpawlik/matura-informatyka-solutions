def fib_list(n):
    fib = [1, 1]
    for i in range(1, n - 1):
        fib.append(fib[i] + fib[i - 1])
    return fib


fibonacci = fib_list(40)
fraktal = []

for i in fibonacci:
    fraktal.append(bin(i)[2::])
for i in fraktal:
    print(i)
print()
for i in fraktal:
    print("0" * (len(fraktal[-1]) - len(i)) + i)
