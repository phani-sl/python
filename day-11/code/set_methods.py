

empty_set = set() # creating an empty set
print(empty_set)

marks = {1, 2, 3, 4, 5} # set of integers
print(marks)
print(type(marks)) # gives the type of the variable

marks.add(7) # adding an element to the set
print("after adding 7", marks)

marks.add(7) # adding a duplicate element to the set
# sets do not allow duplicate elements, so it will not change the set
print("after adding duplicate 7", marks)

marks.copy() # copying the set
print("after copying marks", marks)

marks.clear() # clearing the set
print("after clearing marks", marks)

set_1 = {1, 2, 3, 4, 5, 6} # creating a set_1
print("set_1:", set_1)
set_2 = {2, 5, 7, 8, 9} # creating a set_2
print("set_2:", set_2)

set_1.difference(set_2) # difference method returns a new set with elements in set_1 but not in set_2
print("set_1.difference(set_2):", set_1.difference(set_2))
set_2.difference(set_1) # difference method returns a new set with elements in set_2 but not in set_1
print("set_2.difference(set_1):", set_2.difference(set_1))

set_1.difference_update(set_2) # difference_update method updates set_1 with elements that are in set_1 but not in set_2
print("set_1 after difference_update with set_2:", set_1)
set_2.difference_update(set_1) # difference_update method updates set_2 with elements that are in set_2 but not in set_1
print("set_2 after difference_update with set_1:", set_2)

set_1 = {1, 2, 3, 4, 5, 6} # creating a set_1
print("set_1:", set_1)
set_2 = {2, 5, 7, 8, 9} # creating a set_2
print("set_2:", set_2)

set_1.intersection(set_2) # intersection method returns a new set with elements common to both sets
print("set_1.intersection(set_2):", set_1.intersection(set_2))
set_2.intersection(set_1) # intersection method returns a new set with elements common to both sets
print("set_2.intersection(set_1):", set_2.intersection(set_1))

set_1.intersection_update(set_2) # intersection_update method updates set_1 with elements that are common to both sets
print("set_1 after intersection_update with set_2:", set_1)
set_2.intersection_update(set_1) # intersection_update method updates set_2 with elements that are common to both sets
print("set_2 after intersection_update with set_1:", set_2)

#set_1.remove()
#print("set_1 after removing 2:", set_1)

set_1.discard(3) # discard method removes an element from the set if it exists, does nothing if it doesn't
print("set_1 after discarding 3:", set_1)

set_1 = {1, 2, 3, 4, 5, 6}
print("set_1:", set_1)
set_2 = {2, 5, 7, 8, 9}
print("set_2:", set_2)

set_1.pop() # pop method removes an element from the set 
print("set_1 after popping an element:", set_1)

set_3 = {3, 4}
set_1.issuperset(set_3) # issuperset method checks if set_1 contains all elements of set_3
print("set_1 is superset of set_3:", set_1.issuperset(set_3))

set_3.issubset(set_1) # issubset method checks if set_3 is contained within set_1
print("set_3 is subset of set_1:", set_3.issubset(set_1))

set_1.union(set_2) # union method returns a new set with all elements from both sets
print("set_1.union(set_2):", set_1.union(set_2))

set_2.union(set_1) # union method returns a new set with all elements from both sets
print("set_2.union(set_1):", set_2.union(set_1))

set_1 = {1, 2, 3, 4, 5, 6}
print("set_1:", set_1)
set_2 = {2, 5, 7, 8, 9}
print("set_2:", set_2)

set_1.symmetric_difference(set_2) # symmetric_difference method returns a new set with elements in either set_1 or set_2 but not both
print("set_1.symmetric_difference(set_2):", set_1.symmetric_difference(set_2))
set_2.symmetric_difference(set_1) # symmetric_difference method returns a new set with elements in either set_2 or set_1 but not both
print("set_2.symmetric_difference(set_1):", set_2.symmetric_difference(set_1))

set_1.symmetric_difference_update(set_2) # symmetric_difference_update method updates set_1 with elements that are in either set_1 or set_2 but not both
print("set_1 after symmetric_difference_update with set_2:", set_1)
set_2.symmetric_difference_update(set_1) # symmetric_difference_update method updates set_2 with elements that are in either set_2 or set_1 but not both
print("set_2 after symmetric_difference_update with set_1:", set_2)

print("set_1:", set_1)
print("set_2:", set_2)
print("set_3:", set_3)

set_4 = {10, 11, 12} # creating a new set_4
print("set_4:", set_4)

set_1.isdisjoint(set_2) # isdisjoint method checks if set_1 and set_2 have no elements in common
print("set_1 is disjoint with set_2:", set_1.isdisjoint(set_2))
print("set_1 is disjoint with set_3:", set_1.isdisjoint(set_3))
print("set_2 is disjoint with set_3:", set_2.isdisjoint(set_3))
print("set_1 is disjoint with set_4:", set_1.isdisjoint(set_4))
# isdisjoint method returns True if there are no common elements between the sets
# and False if there are common elements


