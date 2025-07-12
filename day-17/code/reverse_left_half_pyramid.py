

rows = 5
while rows >= 1:
    print("  " * (5 - rows), end="")
    for column in range(1, rows + 1):
        print("* ", end="")
    print()
    rows -= 1

    