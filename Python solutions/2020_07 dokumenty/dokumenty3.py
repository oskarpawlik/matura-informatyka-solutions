file = open("identyfikator.txt", "r")
identyfikatory_temp = []
for i in file:
    identyfikatory_temp.append(i.strip())
identyfikatory = []
for i in identyfikatory_temp:
    identyfikatory.append([i[:3] + i[4:], i[3]])


def reprezentacja_liter(litera):
    return ord(litera) - 55


wagi = [7, 3, 1, 7, 3, 1, 7, 3]

for identyfikator in identyfikatory:
    suma = 0
    for litera in range(8):
        if identyfikator[0][litera].isdigit():
            suma += wagi[litera] * int(identyfikator[0][litera])
        else:
            suma += wagi[litera] * reprezentacja_liter(identyfikator[0][litera])
    if suma % 10 != int(identyfikator[1]):
        print(identyfikator[0][:3] + identyfikator[1] + identyfikator[0][3:])
