rows = 4
for i in range (1, rows+1):
    print(" " * (rows-i), end="")
    for j in range (i):
        print(i, end=" ")
        print()

        