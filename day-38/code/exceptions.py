# Syntax
"""
try:
    # code that may raise multiple types of exceptions
except (ExceptionType1, ExceptionType2, ...):
    # handle both exception types here
"""

# try:
#    num = int(input("Enter a number: "))
#    result = 10 / num
#except (ValueError, ZeroDivisionError):
#    print("Invalid input or division by zero.")

# ValueError occurs if user enters text instead of number.
# ZeroDivisionError occurs if user enters 0.

#try:
#    a = "hello"
#    result = a / 2  # TypeError
#except (TypeError, ZeroDivisionError) as e:
#    print(f"Something went wrong: {e}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Phani", 20)  # __init__ is called
print(p.name, p.age)


class Student:
    def __init__(self, name, roll_no, marks):
        """Initialize attributes when object is created"""
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}"

    def __repr__(self):
        return f"Student(name='{self.name}', roll_no={self.roll_no}, marks={self.marks})"

    def __eq__(self, other):
        """Check equality between two Student objects"""
        if isinstance(other, Student):
            return self.roll_no == other.roll_no
        return False


# Creating objects calls __init__
s1 = Student("A", 101, 88)
s2 = Student("B", 102, 92)
s3 = Student("A", 101, 88)

# Printing objects calls __str__
print(s1)

# calls __repr__
print(repr(s2))

# Equality check (calls __eq__)
print(s1 == s3)  # True 
print(s1 == s2)  # False