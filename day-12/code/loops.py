# loops
# for loop
# while loop

# for loop
'''

syntax:

for value in {sequence}:
    =======================
    =======================
    =====block of code=====
    =======================
    =======================

'''
# for loop with range 
for i in range(10):
    print("i =", i)


fruits = ["apple", "banana", "cherry"]
print(type(fruits))
for fruit in fruits:
    print("fruit =", fruit)
    

vegetables = {"carrot", "broccoli", "spinach"}
print(type(vegetables))
for vegetable in vegetables:
    print("vegetable =", vegetable)
    

for x in range(1, 10):
    print("x =", x)

for char in "python":
    print("char =", char)

for char in "12345":
    print("char =", char)  

# for char in 123456:
    # print("char =", char)  # This will raise an error since integers are not iterable

print("=============")

# while loop
'''

syntax: 

while {condition}:
    =======================
    =======================
    =====block of code=====
    =======================
    =======================
'''
y = 0
# while loop with condition
while y < 10:
    print("y =", y)
    y += 1  # increment y by 1 to avoid infinite loop

total = 3
while total < 10:
    print("total =", total)
    total += 1  # increment total by 1 to avoid infinite loop

sum = 60
while sum > 10:
    print("sum =", sum)
    sum -= 1  # decrement sum by 1 to avoid infinite loop