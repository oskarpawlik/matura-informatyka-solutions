file = open("identyfikator.txt", "r")
identyfikatory_temp = []
for i in file:
    identyfikatory_temp.append(i.strip())
identyfikatory = []
for i in identyfikatory_temp:
    identyfikatory.append([i[0:3], i[3:]])


def is_palindrome(num):
    if num == num[::-1]:
        return True
    return False


for i in identyfikatory:
    if is_palindrome(i[0]) or is_palindrome(i[1]):
        print(i)
