
# Laptop
class Laptop:
    # creating a class attribute
    company = "Electronics"

    # object attributes 
    def __init__ (self, brand, ram, processor, price):
        self.brand = brand
        self.ram = ram
        self.processor = processor
        self.price = price

    # object method
    def show_specs(self):
        print(f"Brand: {self.brand}")
        print(f"Ram: {self.ram}")
        print(f"Processor: {self.processor}")
        print(f"Price: {self.price}")

    # creating class method
    @classmethod
    def display_category (cls):
        print(f"company :{cls.company}")

    # creating static method
    @staticmethod
    def static_method ():
        print("This is a static method example.")

 # creating object 
laptop1 = Laptop("Dell", "8gb", "Intel i7", 50000)

# Calling object (instance) method
laptop1.show_specs()

# Calling class method
Laptop.display_category()

# Calling static method
Laptop.static_method()

print("================")

# Mobile
class Mobile:
    # Class attribute (common to all mobiles)
    category = "Touch Mobiles"

    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage

    # Instance method (object level)
    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Storage: {self.storage}")

    # Class method (class level)
    @classmethod
    def display_category(cls):
        print(f"Category: {cls.category}")

    # Static method (general utility)
    @staticmethod
    def can_make_calls():
        print("Yes, mobiles can make calls.")

# Creating object
m1 = Mobile("Samsung", "Galaxy S21", "128GB")

# Calling instance method
m1.show_details()

# Calling class method
Mobile.display_category()

# Calling static method
Mobile.can_make_calls()

print("================")

# Sun
class Sun:
    galaxy = "Milky Way"

    def __init__(self, temperature, age):
        self.temperature = temperature
        self.age = age

    def show_info(self):
        print(f"Sun's Temperature: {self.temperature} K")
        print(f"Sun's Age: {self.age} billion years")

    @classmethod
    def display_galaxy(cls):
        print(f"The Sun is in the {cls.galaxy} galaxy.")

    @staticmethod
    def is_source_of_light():
        print("Yes.")

sun = Sun(temperature=5778, age=4.6)
sun.show_info()
Sun.display_galaxy()
Sun.is_source_of_light()

print("================")

# Moon
class Moon:
    planet = "Earth"

    def __init__(self, radius, distance_from_earth):
        self.radius = radius  # in kilometers
        self.distance_from_earth = distance_from_earth  # in kilometers

    def show_details(self):
        print(f"Radius: {self.radius} km")
        print(f"Distance from Earth: {self.distance_from_earth} km")

    @classmethod
    def get_planet(cls):
        print(f"The Moon orbits the planet: {cls.planet}")

    @staticmethod
    def has_light():
        print("Yes.")

moon = Moon(radius=17767, distance_from_earth=3788400)
moon.show_details()
Moon.get_planet()
Moon.has_light()

print("================")

# Bottle
class Bottle:
    material_type = "Plastic"

    def __init__(self, brand, capacity):
        self.brand = brand
        self.capacity = capacity  

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Capacity: {self.capacity} ml")

    @classmethod
    def get_material(cls):
        print(f"Most bottles are made of: {cls.material_type}")

    @staticmethod
    def is_reusable():
        print("Depends.")

b1 = Bottle("Bisleri", 1000)
b1.show_info()
Bottle.get_material()
Bottle.is_reusable()

print("================")
