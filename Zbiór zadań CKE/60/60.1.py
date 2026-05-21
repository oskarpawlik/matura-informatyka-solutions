file = open("liczby.txt", "r")
liczby = []
for line in file:
    liczby.append(int(line))
mniejsze = []
for i in liczby:
    if i < 1000:
        mniejsze.append(i)
print("ilosc", len(mniejsze))
print(mniejsze[-2], mniejsze[-1])
