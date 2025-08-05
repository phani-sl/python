
class Parent:
    def __init__(self):
        self._protected_value = 42

    def show(self):
        print("Parent protected value:", self._protected_value)

class Child(Parent):
    def access_protected(self):
        print("Accessed in Child:", self._protected_value)

c = Child()
c.show()
c.access_protected()

""""""

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def _display_balance(self):
        print("Balance is:", self._balance)

class Customer(BankAccount):
    def show_balance(self):
        self._display_balance()

c = Customer(5000)
c.show_balance()