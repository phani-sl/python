def addition(a,b):
    return a + b
res = addition(10, 20)
print("Addition Result:", res)

def subtraction(a, b):
    return a - b 
res = subtraction(20, 10)
print("Subtraction Result:", res)

def multiplication(a, b):
    return a * b
res = multiplication(10, 20)
print("Multiplication Result:", res)

def division(a, b):
    return a / b
res = division(20, 10)
print("Division Result:", res)

def percentile(a, b):
    return a % b
res = percentile(20, 10)
print("Percentile Result:", res)


print("---------------------")


def is_person_eligible_for_vote(age: int, qualified_age: int = 18):
    return age >= qualified_age


res_flag = is_person_eligible_for_vote(10)
print("Is Person Eligible : ", res_flag)

print("---------------------")



def tax_pay(income: int, tax_rate: float = 0.15):
    return income * tax_rate        

res_tax = tax_pay(100000)
print("Tax Payable: ", res_tax)

print("---------------------")



def calculate_area_of_rectangle(length: float, width: float = 5.0):
    return length * width

res_area = calculate_area_of_rectangle(10.0)
print("Area of Rectangle: ", res_area)      

print("---------------------")


