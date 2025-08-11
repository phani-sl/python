class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Number is negative!")
    print("Square is:", num * num)
except NegativeNumberError as e:
    print("Custom Error:", e)
except ValueError:
    print("Please enter a valid integer.")


try:
    num = int("abc")  # Raises ValueError
except Exception:  # This catches everything, so ValueError below never executes
    print("Exception caught")
except ValueError:
    print("ValueError caught")
    

try:
    num = int("abc")
except ValueError:
    print("ValueError caught")
except Exception:
    print("Exception caught")


try:
    data = [1, 2, 3]
    print(data[5])  # IndexError
except ValueError:
    print("ValueError caught")
except IndexError:
    print("IndexError caught")
except Exception:
    print("Generic exception caught")
