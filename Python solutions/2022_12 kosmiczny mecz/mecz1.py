file = open("mecz.txt", "r")
wyniki = file.read().strip()

counter = 0
for i in range(len(wyniki) - 1):
    if wyniki[i] != wyniki[i + 1]:
        counter += 1

print(counter)
