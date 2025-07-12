

empty_set = set()
print(empty_set)

marks = {1, 2, 3, 4, 5}
print(marks)
print(type(marks))

marks.add(7)
print("after adding 7", marks)

marks.add(7)
print("after adding duplicate 7", marks)

marks.copy()
print("after copying marks", marks)

marks.clear()
print("after clearing marks", marks)

set_1 = {1, 2, 3, 4, 5, 6}
print("set_1:", set_1)
set_2 = {2, 5, 7, 8, 9}
print("set_2:", set_2)

set_1.difference(set_2)
print("set_1.difference(set_2):", set_1.difference(set_2))
set_2.difference(set_1)
print("set_2.difference(set_1):", set_2.difference(set_1))

set_1.difference_update(set_2)
print("set_1 after difference_update with set_2:", set_1)
set_2.difference_update(set_1)
print("set_2 after difference_update with set_1:", set_2)

set_1 = {1, 2, 3, 4, 5, 6}
print("set_1:", set_1)
set_2 = {2, 5, 7, 8, 9}
print("set_2:", set_2)

set_1.intersection(set_2)
print("set_1.intersection(set_2):", set_1.intersection(set_2))
set_2.intersection(set_1)
print("set_2.intersection(set_1):", set_2.intersection(set_1))

set_1.intersection_update(set_2)
print("set_1 after intersection_update with set_2:", set_1)
set_2.intersection_update(set_1)
print("set_2 after intersection_update with set_1:", set_2)

#set_1.remove()
#print("set_1 after removing 2:", set_1)

set_1.discard(3)
print("set_1 after discarding 3:", set_1)

set_1 = {1, 2, 3, 4, 5, 6}
print("set_1:", set_1)
set_2 = {2, 5, 7, 8, 9}
print("set_2:", set_2)

set_1.pop()
print("set_1 after popping an element:", set_1)

set_3 = {3, 4}
set_1.issuperset(set_3)
print("set_1 is superset of set_3:", set_1.issuperset(set_3))

set_3.issubset(set_1)
print("set_3 is subset of set_1:", set_3.issubset(set_1))

set_1.union(set_2)
print("set_1.union(set_2):", set_1.union(set_2))

set_2.union(set_1)
print("set_2.union(set_1):", set_2.union(set_1))

set_1 = {1, 2, 3, 4, 5, 6}
print("set_1:", set_1)
set_2 = {2, 5, 7, 8, 9}
print("set_2:", set_2)

set_1.symmetric_difference(set_2)
print("set_1.symmetric_difference(set_2):", set_1.symmetric_difference(set_2))
set_2.symmetric_difference(set_1)   
print("set_2.symmetric_difference(set_1):", set_2.symmetric_difference(set_1))

set_1.symmetric_difference_update(set_2)
print("set_1 after symmetric_difference_update with set_2:", set_1)
set_2.symmetric_difference_update(set_1)
print("set_2 after symmetric_difference_update with set_1:", set_2)


