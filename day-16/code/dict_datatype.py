
dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False,
}

print(type(dict))  
print(dict)  

# Accessing values
print(dict.get("name"))  
print(dict.get("age")) 
print(dict.get("city"))  
print(dict.get("is_student"))

keys_set = dict.keys()
values = dict.values()

print(keys_set)
print(values)

for key in dict:
    print(dict.get(key))

# pop method
value = dict.pop("age")  # Removes the key "age" and returns its value
print(value)  
print(dict)   

# clear method
dict.clear()  # Removes all items from the dictionary
print(dict)  

