
# Single Inheritance
"""
 A child class inherits from only one parent class.
"""
class Animal:
    def sound(self):
        print("Animals make sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog barks.")

d = Dog()
d.sound()
d.bark()


# Mutlipe Inheritance
"""
A child class inherits from more than one parent class.
"""
class Father:
    def skills(self):
        print("Gardening, Driving")

class Mother:
    def skills(self):
        print("Cooking, Painting")

class Child(Father, Mother):
    def own_skills(self):
        print("Programming")

c = Child()
c.skills()        # Will call Father's skills (because Father is first in inheritance order)
c.own_skills()


# Multilevel Inheritance
"""
A class inherits from a child class, making a chain of inheritance.
"""
class Grandparent:
    def house(self):
        print("Grandparent's House")

class Parent(Grandparent):
    def car(self):
        print("Parent's Car")

class Child(Parent):
    def bike(self):
        print("Child's Bike")

c = Child()
c.house()
c.car()
c.bike()


# Hierarchical Inheritance
"""
Multiple child classes inherit from a single parent class.
"""
class Vehicle:
    def info(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def wheels(self):
        print("Car has 4 wheels.")

class Bike(Vehicle):
    def wheels(self):
        print("Bike has 2 wheels.")

c = Car()
b = Bike()

c.info()
c.wheels()
b.info()
b.wheels()


# Hybrid Inheritance
"""
A combination of two or more types of inheritance.
"""
class A:
    def show(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(A):
    def show_c(self):
        print("Class C")

class D(B, C):  # Hybrid: Multiple inheritance from B and C
    def show_d(self):
        print("Class D")

d = D()
d.show()     # Inherited from class A via B or C
d.show_b()
d.show_c()
d.show_d()
