import math
from wsgiref.util import request_uri

file = open("liczby.txt", "r")
liczby = []
for line in file:
    liczby.append(int(line))


def czy_18_dzielnikow(n):
    dzielniki = []
    for i in range(1, n + 1):
        if n % i == 0:
            dzielniki.append(i)
    if len(dzielniki) == 18:
        return dzielniki
    return False


for i in liczby:
    if czy_18_dzielnikow(i) != False:
        print(czy_18_dzielnikow(i), czy_18_dzielnikow(i)[-1])
