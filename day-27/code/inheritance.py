
# Examples on Inheritance

class Parent:
    def __init__(self):
        self.name = "PARENT"

    def display_info(self):
        print("Parent Name: ", self.name)


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class initialized.")

    def child_info(self):
        print("Accessing Child class info:")

child =Child() # Child object will be aquired properties and methods of Parent class And then child object will be created.
print("Child Name: ", child.name)  # Accessing Parent class attribute
child.child_info()
child.display_info()  # Accessing Parent class method

print("=======================")

class Animal:
    def __init__(self):
        self.species = "Animal"

    def display_info(self):
        print("Species Type: ", self.species)


class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("cat class initialized.")

    def cat_info(self):
        print("Accessing Cat Class info:")


name = Cat()
print("Species Name: ", name.species)
name.cat_info()
name.display_info()

print("=======================")

class Ranks:
    def __init__(self):
        self.type = "Ranks"

    def display_info(self):
        print("Information Of: ", self.type)


class Diamond(Ranks):
    def __init__(self):
        super().__init__()
        print("diamond class initialized.")

    def diamond_info(self):
        print("Accessing Diamond Class info:")

place = Diamond()
print("Rank Type: ",  place.type)
place.diamond_info()
place.display_info()

