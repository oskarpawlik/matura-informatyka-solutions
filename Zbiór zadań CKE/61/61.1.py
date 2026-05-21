file = open("ciagi.txt", "r")
ciagi = []
for i in file:
    if len(i.strip().split()) == 1:
        continue
    else:
        ciagi.append(i.strip().split())


def is_array(arr):
    r = int(arr[1]) - int(arr[0])
    for i in range(len(arr) - 1):
        if int(arr[i + 1]) - int(arr[i]) != r:
            return False
    return True


true_arrays = []
for i in ciagi:
    if is_array(i):
        true_arrays.append(i)
print("ciagi arytmetyczne", len(true_arrays))
R = 0
for arr in range(len(true_arrays)):
    if int(true_arrays[arr][1]) - int(true_arrays[arr][0]) > R:
        R = int(true_arrays[arr][1]) - int(true_arrays[arr][0])
print("najwieksza roznica", R)
