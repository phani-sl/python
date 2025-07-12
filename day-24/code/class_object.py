
class Laptop:
    # Class-level attribute 
    category = "Electronics"

    def __init__(self, brand, ram, processor):
        self.brand = brand        # Object-level attribute
        self.ram = ram            # Object-level attribute
        self.processor = processor  # Object-level attribute

    # Object-level method (uses self)
    def show_specs(self):
        print("Laptop Specifications:")
        print("Brand :" , self.brand)
        print("RAM :" , self.ram)
        print("Processor :" , self.processor)

    # Class-level method (uses cls)
    @classmethod
    def category(cls, category):
        cls.category = category
        print("Category : ",cls.category)

# Creating objects
laptop1 = Laptop("Dell", "16GB", "Intel i7")
laptop2 = Laptop("HP", "8GB", "AMD Ryzen 5")

print("Accessing Class Level Variable using Object:", Laptop.category)
print("Accessing Class Level Method using Object:")

laptop1.show_specs()  # Calling class method using object
print("--------")
laptop2.show_specs()

print("Category Name:", Laptop.category)  # Accessing class variable




    