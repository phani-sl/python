# creating an empty list
empty_list = []
print("empty list", empty_list)

# creating a list of even numbers from 5 to 20
even_numbers_from_5_20: list = [6, 8, 10, 12, 14, 16, 18]
print("even numbers from 5 to 20", even_numbers_from_5_20)

# datatype
print("datatype of even numbers from 5 to 20", type(even_numbers_from_5_20))

# adding 20 to the list
# using append() we can add an single element to the existing list
even_numbers_from_5_20.append(20)
print("after appending", even_numbers_from_5_20)

# to add multiple elements to the existing list then we create another list and using extend() method we can add a list
other_numbers_upto_30 = [22, 24, 26, 28]
even_numbers_from_5_20.extend(other_numbers_upto_30)
print("after extending", even_numbers_from_5_20)

# to remove any of the element present in the list we use remove() method
even_numbers_from_5_20.remove(18)
print("after removing 18", even_numbers_from_5_20)

# to insert any element at the specific position. then using its index number as position.
# we use insert() method and insert the value.
even_numbers_from_5_20.insert(0, 4)
print("after inserting 4 at index 0", even_numbers_from_5_20)

# to arrange the elements in list in ascending order we use sort() method.
even_numbers_from_5_20.sort()
print("after sorting in ascending order", even_numbers_from_5_20)

# to sort in descending order we use sort(reverse=True) method.
even_numbers_from_5_20.sort(reverse=True)
print("after sorting in descending order", even_numbers_from_5_20)

# it removes index based element
even_numbers_from_5_20.pop(5)
print("after popping index 5", even_numbers_from_5_20)

# copy the same list
even_numbers_from_5_20.copy()
print("copy of the list", even_numbers_from_5_20)

# adding 6 to the list
even_numbers_from_5_20.append(6)
print("after adding 6 to the list", even_numbers_from_5_20)

# size of the list
print("size of the list", len(even_numbers_from_5_20))

# to know how many times a specific element is present in the list
count_6 = even_numbers_from_5_20.count(6)
print("count of 6 in the list", count_6)

# to clear a list we use clear() method
even_numbers_from_5_20.clear()
print("after clearing the list", even_numbers_from_5_20)


users: list = []
others = ['b', 'c', 'd', 'e', 'f']

users.append('a') # 'a'
users.extend(others) # 'a', 'b', 'c', 'd', 'e', 'f'
users.remove('b') # 'a', 'c', 'd', 'e', 'f'
users.pop(2) # 'a', 'c', 'e', 'f' # to perform pop() method use index number
users.copy() # 'a', 'c', 'e', 'f'
users.reverse() # 'f', 'e', 'c', 'a'
users.sort() # 'a', 'c', 'e', 'f'
users.insert(1, 'b') # use index position and new element

index = users.index('f')
print("after performing index :", index)

count = users.count('a')
print("after counting :", count)

users.clear()

print(users)
