
# round

f: float = 36.76 # converts decimal value to complete number. here after decimal point it is greater than 5.
print(f"round({f}) =", round(f))

f = 43.5 # here the the digit after decimal point is equal to 5. it gives greater value.
print(f"round({f}) =", round(f))

f = 27.333 # here the digit after decimal point is less than 5. so it prints same value.
print(f"round({f}) =", round(f))

print("===============================")

# abs
# converts negative value to postive value.

a = -32 # converts negative value to positive value.
print(f"abs({a}) =", abs(a))

a = 43.67 # positive value remains same.
print(f"abs({a}) =", abs(a))

print("abs(-0.333) =", abs(-0.333)) 

print("================================")

# pow
# raised to the power of

print("pow(2, 6) =", pow(2, 6)) # 2 raised to the power of 6

print("pow(3.34, 3) =", pow(3.34, 3)) # 3.34 raised to the power of 3

print("pow(2, -3) =", pow(2, -3)) # 2 raised to the power of -3 (which is 1/8)

print("pow(-4, 2) =", pow(-4, 2)) # -4 raised to the power of 2

'''

if any of the value is negative then it converts to p/q form 

'''

print("pow(2, 0) =", pow(2, 0)) # 2 raised to the power of 0 (which is 1)


print("=================================")


#divmod
# returns quotient and remainder

print("divmod(10,2) =", divmod(10,2))

print("divmod(10,3) =", divmod(10,3)) 

print("divmod(-24,4) =", divmod(-24,4))

print("divmod(0,6) =", divmod(0,6))

# 
# print("divmod(6,0) =", divmod(6,0))
# this will give error because division by zero is not allowed

print("=================================")


# min

print("min(10, 20, 30) =", min(10, 20, 30))  # returns the smallest value
print("min(10, 20, 30, -5) =", min(10, 20, 30, -5))  # returns the smallest value including negative
print("min(10.5, 20.3, 30.1) =", min(10.5, 20.3, 30.1))  # returns the smallest float value
print("min('a','bc') =", min('a','bc'))  # returns the smallest string value


print("==================================")

# max

print("max(10, 20, 30) =", max(10, 20, 30))  # returns the largest value
print("max(10, 20, 30, -5) =", max(10, 20, 30, -5))  # returns the largest value including negative 
print("max(10.5, 20.3, 30.1) =", max(10.5, 20.3, 30.1))  # returns the largest float value
print("max('a','bc') =", max('a','bc'))  # returns the largest string value

print("==================================")







