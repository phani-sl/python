
# packing and unpacking tuples
# packing is when you create a tuple with multiple values
tuple_2 = (4, 5, 6, 7, 8, 9,)

# unpacking is when you extract values from a tuple
a, b, c, d, e, f = tuple_2 
print(a)  
print(b)  
print(c)  

# you can also unpack with an asterisk to collect remaining values
tuple_3 = (7, 8, 9, 10)
a, *b = tuple_3
print(a)  # 7
print(b)  # [8, 9, 10]

# discarding values during unpacking
a, b, c, _ = tuple_3  # discarding the second value
print(a)  # 7
print(c)  # 9
print(tuple_3)  # (7, 8, 9, 10)

# unpacking with fewer variables than values
# this will raise a ValueError
# a, b = tuple_3 
# # ValueError: too many values to unpack (expected 2)
