file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(int(i))

liczby_hex = []
for i in liczby:
    liczby_hex.append(hex(i)[2::])


liczby_ilosc = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
}

for liczba in liczby_hex:
    for znak in liczba:
        liczby_ilosc[znak] += 1

for i in liczby_ilosc:
    print(i, ":", liczby_ilosc[i])
