file = open("ciagi.txt", "r")
liczby_bin = []
for i in file:
    liczby_bin.append(i.strip())
liczby_dec = []
for i in liczby_bin:
    liczby_dec.append(int(i, 2))


def czy_pol_pierwsza(n):
    czynniki = []
    i = 2
    while n > 1:
        if n % i == 0:
            czynniki.append(i)
            n = n / i
            i = 1
        i += 1
        if len(czynniki) > 2:
            return False
    if len(czynniki) == 2:
        return True
    return False


pol_pierwsze_liczby = []
for i in liczby_dec:
    if czy_pol_pierwsza(i):
        pol_pierwsze_liczby.append(i)
print(len(pol_pierwsze_liczby))
print("max", max(pol_pierwsze_liczby))
print("min", min(pol_pierwsze_liczby))
