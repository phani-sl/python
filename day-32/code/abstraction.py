from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# shape = Shape()  # Can't instantiate abstract class
rect = Rectangle(5, 10)
print(rect.area())  # 50


from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

    def move(self):
        return "Runs on four legs"

dog = Dog()
print(dog.sound())  # Bark
print(dog.move())   # Runs on four legs

class Calculator:
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(5, 3))       # 8
print(calc.multiply(4, 2))  # 8


from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    
    @abstractmethod
    def area(self):  # Abstract method
        pass
    
    def description(self):  # Concrete method
        return "This is a shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Must implement abstract method
        return 3.14 * self.radius ** 2

# Using the class
circle = Circle(5)
print(circle.description())  # Concrete method from abstract class
print("Area:", circle.area())

from abc import ABC

class MyClass(ABC):  # Abstract base class
    def greet(self):
        print("Hello from MyClass")

# Instantiation is allowed
obj = MyClass()
obj.greet()
