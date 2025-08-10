list_ex  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(max(list_ex))

max_num = list_ex[0]
for i in range(len(list_ex)):
    max_num = list_ex[i] if list_ex[i] > max_num else max_num

print(max_num)

print(min(list_ex))

min_num = list_ex[0]
for i in range(len(list_ex)):
    min_num = list_ex[i] if list_ex[i] < min_num else min_num

print(min_num)
