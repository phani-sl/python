# a = 10
# b = 0
# print(a / b)  # This will raise ZeroDivisionError

""""""

# print(name) # This will raise NameError

""""""

# num = int("abc")  # This will raise ValueError

""""""

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

""""""

try:
    print(x)  # x is not defined
except NameError:
    print("Variable is not defined!")

""""""

try:
    num = int("abc")  # Invalid conversion
except ValueError:
    print("You entered an invalid number!")

""""""