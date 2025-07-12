rows = 5
for i in range (1, rows+1):
    print("* " * i + " " * (2 * (rows - 1)) + "* " * i)
for i in reversed (range(1, rows+1)):
    print("* " * i + " " * (2 * (rows - 1)) + "* " * i)
    