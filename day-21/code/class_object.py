
# laptop

class Laptop:
    def __init__(self, brand, ram, processor):
        self.brand = brand
        self.ram = ram
        self.processor = processor

    def specs(self):
        print("laptop brand:", self.brand)
        print("laptop ram:", self.ram)
        print("laptop processor:", self.processor)

l1 = Laptop(brand="Dell", ram="16GB", processor="Intel i7")
l1.specs()
print("l1 =", l1)
print(type(l1))



# Mobile

class Mobile:
    def __init__(self, brand, ram, processor):
        self.brand = brand
        self.ram = ram
        self.processor = processor

    def specs(self):
        print("mobile brand:", self.brand)
        print("mobile ram:", self.ram)
        print("mobile processor:", self.processor)

m1 = Mobile(brand="Samsung", ram="8GB", processor="Exynos 990")
m1.specs()
print("m1 =", m1)
print(type(m1))



# Sun

class Sun:
    def __init__(self, name, radius, temperature):
        self.name = name
        self.radius = radius
        self.temperature = temperature

    def details(self):
        print("Sun name:", self.name)
        print("Sun radius:", self.radius)
        print("Sun temperature:", self.temperature)

s1 = Sun(name="Sun", radius="696340 km", temperature="5505 K")
s1.details()
print("s1 =", s1)
print(type(s1))



# Moon

class Moon:
    def __init__(self, name, radius, temperature):
        self.name = name
        self.radius = radius
        self.temperature = temperature

    def details(self):
        print("Moon name:", self.name)
        print("Moon radius:", self.radius)
        print("Moon temperature:", self.temperature)

m1 = Moon(name="Moon", radius="1737.4 km", temperature="-53 °C")
m1.details()
print("m1 =", m1)
print(type(m1))



# File

class File:
    def __init__(self, name, size, file_type):
        self.name = name
        self.size = size
        self.file_type = file_type

    def details(self):
        print("File name:", self.name)
        print("File size:", self.size)
        print("File type:", self.file_type)

f1 = File(name="document.txt", size="15KB", file_type="Text")
f1.details()
print("f1 =", f1)
print(type(f1))



# Mouse

class Mouse:
    def __init__(self, brand, dpi, wireless):
        self.brand = brand
        self.dpi = dpi
        self.wireless = wireless

    def specs(self):
        print("Mouse brand:", self.brand)
        print("Mouse DPI:", self.dpi)
        print("Mouse wireless:", self.wireless)

m1 = Mouse(brand="Logitech", dpi="16000", wireless=True)
m1.specs()
print("m1 =", m1)
print(type(m1))



# Bottle

class Bottle:
    def __init__(self, material, capacity, color):
        self.material = material
        self.capacity = capacity
        self.color = color

    def details(self):
        print("Bottle material:", self.material)
        print("Bottle capacity:", self.capacity)
        print("Bottle color:", self.color)

b1 = Bottle(material="Plastic", capacity="500ml", color="Blue")
b1.details()
print("b1 =", b1)
print(type(b1))



# XYZ
class XYZ:
    def __init__(self, attribute1, attribute2, attribute3):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3

    def display(self):
        print("XYZ attribute1:", self.attribute1)
        print("XYZ attribute2:", self.attribute2)
        print("XYZ attribute3:", self.attribute3)

xyz1 = XYZ(attribute1="Value1", attribute2="Value2", attribute3="Value3")
xyz1.display()
print("xyz1 =", xyz1)
print(type(xyz1))



# Microchip

class Microchip:
    def __init__(self, model, speed, technology):
        self.model = model
        self.speed = speed
        self.technology = technology

    def info(self):
        print("Microchip model:", self.model)
        print("Microchip speed:", self.speed)
        print("Microchip technology:", self.technology)
mchip1 = Microchip(model="XYZ123", speed="3.5GHz", technology="7nm")
mchip1.info()
print("mchip1 =", mchip1)
print(type(mchip1))


