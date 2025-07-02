
"""
tuple :
a tuple is a collection of items. items in a tuple are ordered and its allows to have duplicate items.
"""

'''
syntax:
tuple_name = (item1, item2, item3, ...)
'''
# tuple with same data type
tuple_1 = (1, 2, 3, 4,)

# tuple with different data type
tuple_2 = (1, "hello", 3.14, True)

# tuple without parentheses
tuple_3 = 1, 2, 3, 4
tuple_4 = 1, "hello", 3.14, True

# tuple with single item
tuple_5 = (1,)  # Note the comma
tuple_6 = 1,  # Note the comma

# empty tuple
tuple_7 = ()

tuple_8 = (5)
tuple_9 = 5

print("tuple_1:", tuple_1)
print("tuple_2:", tuple_2)
print("tuple_3:", tuple_3)
print("tuple_4:", tuple_4)
print("tuple_5:", tuple_5)
print("tuple_6:", tuple_6)
print("tuple_7:", tuple_7)
print("tuple_8:", tuple_8)
print("tuple_9:", tuple_9)

print("Type of tuple_1:", type(tuple_1))
print("Type of tuple_2:", type(tuple_2))
print("Type of tuple_3:", type(tuple_3))
print("Type of tuple_4:", type(tuple_4))
print("Type of tuple_5:", type(tuple_5))
print("Type of tuple_6:", type(tuple_6))
print("Type of tuple_7:", type(tuple_7))
print("Type of tuple_8:", type(tuple_8))
print("Type of tuple_9:", type(tuple_9))

# tuple_8 and tuple_9 are not tuples, they are just integers
# tuple_8 is an integer because it is not enclosed in parentheses
# tuple_9 is also an integer for the same reason

# accessing tuple elements
print("first element of tuple_1:", tuple_1[0])  
print("second element of tuple_2:", tuple_2[1])  


