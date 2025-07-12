def print_diamond(n):
    # Upper half 0, 4 => 1, 3,5, 7, 9 =>    rrow_index+1=> 0+1=1, 2*1+1 = 3,   2*2+1 =5
    for row_index in range(n):  # first iteration => i=0, n=5
        # 2nd iteration => i=1, n=5

        space_calculation = n - row_index - 1  # 5-0-1 = 4 spaces,  5-1-1 = 3 spaces

        star_calculation = 2 * row_index + 1  # 2*0+1 = 1 star, 2* 1 +1
        print("  " * space_calculation + "* " * star_calculation)
        """
        n=5
        i=1
        " "*3
        """

    # Lower half
    for i in range(n - 2, -1, -1):
        print("  " * (n - i - 1) + "* " * (2 * i + 1))


print_diamond(5)


