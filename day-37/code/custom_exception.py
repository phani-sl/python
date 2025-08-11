# Custom exception class
class MyCustomError(Exception):
    pass

# Example usage
try:
    raise MyCustomError("Something went wrong!")
except MyCustomError as e:
    print("Caught custom exception:", e)


class AgeTooLowError(Exception):
    def __init__(self, age, message="Age is below the allowed limit"):
        self.age = age
        self.message = message
        super().__init__(f"{message}. Provided age: {age}")

# Example usage
try:
    age = 15
    if age < 18:
        raise AgeTooLowError(age)
except AgeTooLowError as e:
    print(e)
    print("Age value in exception object:", e.age)


class NegativeValueError(Exception):
    pass

class ValueTooLargeError(Exception):
    pass

def check_value(num):
    if num < 0:
        raise NegativeValueError("Negative values are not allowed!")
    elif num > 100:
        raise ValueTooLargeError("Value exceeds the allowed maximum!")
    else:
        print("Value is valid.")

try:
    check_value(150)
except NegativeValueError as e:
    print("Negative Value Error:", e)
except ValueTooLargeError as e:
    print("Too Large Error:", e)


class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong!")
except MyError as e:
    print("Caught MyError:", e)


class InvalidUsernameError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

def login(username, password):
    if username != "admin":
        raise InvalidUsernameError("Username is incorrect")
    if password != "1234":
        raise InvalidPasswordError("Password is incorrect")
    print("Login successful!")

try:
    login("user", "1234")
except InvalidUsernameError as e:
    print("Username Error:", e)
except InvalidPasswordError as e:
    print("Password Error:", e)