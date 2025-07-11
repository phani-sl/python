
# laptop

class Laptop:
    category = "Electronics"  # Class attribute

    def __init__(self, brand, ram, processor):
        self.brand = brand
        self.ram = ram
        self.processor = processor

    def specs(self):  # Object method
        print("Laptop Brand:", self.brand)
        print("RAM:", self.ram)
        print("Processor:", self.processor)

    @classmethod
    def get_category(cls):  # Class method
        print("Category:", cls.category)
    
l1 = Laptop(brand="Dell", ram="16GB", processor="Intel i7")
l1.specs()
l1.get_category()  # Call class method
print("l1 =", l1)
print(type(l1))

# Mobile
class Mobile:
    category = "Electronics"  # Class attribute

    def __init__(self, brand, ram, processor):
        self.brand = brand
        self.ram = ram
        self.processor = processor

    def specs(self):  # Object method
        print("Mobile Brand:", self.brand)
        print("RAM:", self.ram)
        print("Processor:", self.processor)

    @classmethod
    def get_category(cls):  # Class method
        print("Category:", cls.category)
m1 = Mobile(brand="Samsung", ram="8GB", processor="Exynos 990")
m1.specs()
m1.get_category()  # Call class method
print("m1 =", m1)
print(type(m1))

# Sun
class Sun:
    category = "Celestial Body"  # Class attribute

    def __init__(self, name, radius, temperature):
        self.name = name
        self.radius = radius
        self.temperature = temperature

    def details(self):  # Object method
        print("Sun Name:", self.name)
        print("Radius:", self.radius)
        print("Temperature:", self.temperature)

    @classmethod
    def get_category(cls):  # Class method
        print("Category:", cls.category)
s1 = Sun(name="Sun", radius="696340 km", temperature="5505 K")
s1.details()
s1.get_category()  # Call class method
print("s1 =", s1)
print(type(s1))

# Moon
class Moon:
    category = "Celestial Body"  # Class attribute

    def __init__(self, name, radius, temperature):
        self.name = name
        self.radius = radius
        self.temperature = temperature

    def details(self):  # Object method
        print("Moon Name:", self.name)
        print("Radius:", self.radius)
        print("Temperature:", self.temperature)

    @classmethod
    def get_category(cls):  # Class method
        print("Category:", cls.category)
m1 = Moon(name="Moon", radius="1737.4 km", temperature="-53 °C")
m1.details()
m1.get_category()  # Call class method
print("m1 =", m1)
print(type(m1))

# File
class File:
    category = "Storage"  # Class attribute

    def __init__(self, name, size, file_type):
        self.name = name
        self.size = size
        self.file_type = file_type

    def details(self):  # Object method
        print("File Name:", self.name)
        print("Size:", self.size)
        print("Type:", self.file_type)

    @classmethod
    def get_category(cls):  # Class method
        print("Category:", cls.category)
f1 = File(name="document.txt", size="15KB", file_type="Text")
f1.details()
f1.get_category()  # Call class method
print("f1 =", f1)
print(type(f1))

# Mouse
class Mouse:
    category = "Peripheral"  # Class attribute

    def __init__(self, brand, type, dpi):
        self.brand = brand
        self.type = type
        self.dpi = dpi

    def details(self):  # Object method
        print("Mouse Brand:", self.brand)
        print("Type:", self.type)
        print("DPI:", self.dpi)

    @classmethod
    def get_category(cls):  # Class method
        print("Category:", cls.category)
m1 = Mouse(brand="Logitech", type="Wireless", dpi="16000")
m1.details()
m1.get_category()  # Call class method
print("m1 =", m1)
print(type(m1))

# Bottle
class Bottle:
    category = "Container"  # Class attribute

    def __init__(self, material, capacity, color):
        self.material = material
        self.capacity = capacity
        self.color = color

    def details(self):  # Object method
        print("Bottle Material:", self.material)
        print("Capacity:", self.capacity)
        print("Color:", self.color)

    @classmethod
    def get_category(cls):  # Class method
        print("Category:", cls.category)
b1 = Bottle(material="Plastic", capacity="500ml", color="Blue")
b1.details()
b1.get_category()  # Call class method
print("b1 =", b1)
print(type(b1))

# Microchip 
class Microchip:
    category = "Electronics"  # Class attribute

    def __init__(self, model, size, technology):
        self.model = model
        self.size = size
        self.technology = technology

    def details(self):  # Object method
        print("Microchip Model:", self.model)
        print("Size:", self.size)
        print("Technology:", self.technology)

    @classmethod
    def get_category(cls):  # Class method
        print("Category:", cls.category)
        print("Microchip Category:", cls.category)
mc1 = Microchip(model="XYZ123", size="5mm", technology="CMOS")
mc1.details()
mc1.get_category()  # Call class method
print("mc1 =", mc1)
print(type(mc1))

