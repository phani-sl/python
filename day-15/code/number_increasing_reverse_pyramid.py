rows = 4

for i in range(rows):
    count = 1
    for j in range(rows - i):
        print(count, end=" ")
        count += 1
    print()
