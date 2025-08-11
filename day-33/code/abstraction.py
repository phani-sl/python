from abc import ABC, abstractmethod

class Validator(ABC):
    @staticmethod
    def is_positive(number):
        return number > 0

    @abstractmethod
    def validate(self):
        pass

class PositiveNumberValidator(Validator):
    def __init__(self, number):
        self.number = number

    def validate(self):
        return Validator.is_positive(self.number)

obj = PositiveNumberValidator(10)
print(obj.validate())  # True

from abc import ABC, abstractmethod

class Shape(ABC):
    shape_count = 0  # Class-level variable

    def __init__(self, color):
        self.color = color  # Instance variable
        Shape.shape_count += 1

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        from math import pi
        return pi * self.radius ** 2

c1 = Circle(5, "Red")
c2 = Circle(3, "Blue")

print(Shape.shape_count)  # 2 (shared)
print(c1.color, c1.area())  # Red 78.53...
print(c2.color, c2.area())  # Blue 28.27...


from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
        print(f"Vehicle created: {brand}")

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.brand} car engine started.")


# v = Vehicle("Generic")  # ERROR: Can't instantiate abstract class
c = Car("Toyota")          #  Works
c.start_engine()

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id):
        self.emp_id = emp_id
        print(f"Employee ID set: {emp_id}")

    @abstractmethod
    def calculate_salary(self):
        pass


class Developer(Employee):
    def __init__(self, emp_id, skill):
        super().__init__(emp_id)  # Call parent's __init__
        self.skill = skill
        print(f"Skill: {skill}")

    def calculate_salary(self):
        print(f"Salary calculated for developer {self.emp_id}")


dev = Developer(101, "Python")
dev.calculate_salary()

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, brand):
        print("Vehicle __init__ called")
        self.brand = brand

    @abstractmethod
    def start_engine(self):
        pass


# Concrete class
class Car(Vehicle):
    def __init__(self, brand, model):
        print("Car __init__ called")
        # Call parent class's __init__
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine started.")


# Using the concrete class
my_car = Car("Toyota", "Corolla")
print(my_car.brand)  # from abstract class __init__
print(my_car.model)  # from concrete class __init__
my_car.start_engine()
