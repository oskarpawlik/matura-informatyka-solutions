file = open("liczby.txt", "r")
liczby = []
for i in file:
    liczby.append(i.strip())
sumy = []
for i in liczby:
    sumy.append(str(int(i) + int(i[::-1])))


def is_palindrome(s):
    if s == s[::-1]:
        return True
    return False


counter = 0
for i in sumy:
    if is_palindrome(i):
        counter += 1
print(counter)
