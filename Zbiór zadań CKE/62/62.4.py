file = open("liczby2.txt", "r")
liczby = []
for line in file:
    liczby.append(int(line.strip()))
longstring_dec = ""
for i in liczby:
    longstring_dec += str(i)
print("dziesietnie", longstring_dec.count("6"))
liczby_oct = []
for i in liczby:
    liczby_oct.append(oct(i)[2::])
longstring_oct = ""
for i in liczby_oct:
    longstring_oct += i
print("osemkowe", longstring_oct.count("6"))
