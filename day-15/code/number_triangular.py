rows = 4
columns = 7
mid = rows
for row in range(1, rows+1):
    print((mid-row)* " ", end="")
    for time in range(1, row+1):
         print(f"{row} ", end="")
    print()
   