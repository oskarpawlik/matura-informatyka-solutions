file = open("mecz.txt", "r")
wyniki = file.read().strip()


def licz_wyniki(wynik):
    A = 0
    B = 0
    for i in wynik:
        if i == "A":
            A += 1
        else:
            B += 1
        if (A >= 1000 or B >= 1000) and abs(A - B) >= 3:
            if A == max(A, B):
                return "A", A, B
            return "B", B, A


print(licz_wyniki(wyniki))
