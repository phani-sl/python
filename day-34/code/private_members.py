
class Student:
    def __init__(self):
        self.__marks = 90  # private variable

    def show_marks(self):
        print("Marks:", self.__marks)

s = Student()
s.show_marks() # Access inside class
# print(s.__marks)  cannot access directly

""""""

class Employee:
    def __init__(self, name, id, salary):
        self.name = name  # Public Member
        self._id = id  # Protected Member => Id can be known by some people like you team members,
        self.__salary = salary  # Private to Employee


emp = Employee("Phani", 2345, 32432)
print("name: ", emp.name)

""""""

class UserDetatils:

    def __init__(self, user_number, name, type):
        #   Secured the members of the class.
        self.__name = name
        self.__user_number = user_number
        self.__type = type

    def get_name(self):
        return self.__name

    def get_account_number(self):
        return self.__user_number

    def get_type(self):
        return self.__type

    def set_name(self, name):
        self.__name = name

    def set_account_number(self, user_number):
        self.__account_number = user_number

    def set_type(self, type):
        self.__type = type


Account = UserDetatils("78377390", "Phani", "Student")

print(Account.get_name())
Account.set_name("Mohan")
print(Account.get_name())