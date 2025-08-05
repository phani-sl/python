
class Student:
    def __init__(self, name, age):
        self.name = name     # public variable
        self.age = age       # public variable

s = Student("Phani", 20)
print(s.name)   # Accessing public member
print(s.age)

""""""

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def show_info(self):
        print("Brand:", self.brand)
        print("Speed:", self.speed)

c = Car("Tata", 200)
c.show_info()           # Accessing public method
print(c.brand)          # Accessing public variable

""""""

class Book:
    def __init__(self, title):
        self.title = title  # public member

b = Book("Python Basics")
print(b.title)         # Python Basics

b.title = "Advanced Python"  # Changing public member
print(b.title)         # Advanced Python