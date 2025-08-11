def process_data():
    try:
        value = int("abc")  # Will raise ValueError
    except ValueError:
        print("Logging: Invalid integer found")
        raise  # Rethrows the same ValueError

try:
    process_data()
except ValueError as e:
    print(f"Caught in caller: {e}")


def read_file():
    try:
        with open("non_existent.txt") as f:
            f.read()
    except FileNotFoundError as e:
        print("File not found, rethrowing...")
        raise e

try:
    read_file()
except FileNotFoundError as e:
    print(f"Handled in caller: {e}")


# Built-in exception object
ex1 = ValueError("Invalid value provided")

# Custom exception class
class MyError(Exception):
    pass

ex2 = MyError("Something went wrong!")

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    divide(10, 0)
except ZeroDivisionError as e:
    print(f"Caught exception: {e}")

class NegativeNumberError(Exception):
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return True

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(f"Caught custom exception: {e}")

try:
    print("Inside try")
    x = 1 / 0
except ZeroDivisionError:
    print("Caught division error")
finally:
    print("Finally always runs")

print("Program continues...")

try:
    num = int("123")
except ValueError:
    print("Invalid number")
else:
    print("Conversion successful:", num)

try:
    data = [1, 2, 3]
    print(data[1])
except IndexError:
    print("Invalid index")
else:
    print("Index was valid")
finally:
    print("Always runs")

try:
    nums = [1, 2, 3]
    print(nums[3])
except IndexError:
    print("Index out of range.")
except ZeroDivisionError:
    print("Division by zero.")
else:
    print("No exception occurred.")
finally:
    print("Always runs.")

class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("Something went wrong!")
except MyCustomError as e:
    print("Caught custom exception:", e)

class AppError(Exception):
    """Base class for all app-specific exceptions."""
    pass

class FileFormatError(AppError):
    pass

class DatabaseConnectionError(AppError):
    pass

try:
    raise DatabaseConnectionError("Database is not reachable!")
except FileFormatError:
    print("File format problem.")
except DatabaseConnectionError as e:
    print("Database error:", e)
except AppError:
    print("General app error.")

try:
    raise ValueError("This is allowed")  # Inherits from Exception → BaseException
except ValueError as e:
    print("Caught ValueError:", e)

try:
    raise 404   # Not a BaseException
except Exception as e:
    print("Caught:", type(e), e)
