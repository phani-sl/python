a=12
b=19


# if condition
if a > b:
    print("a is greater than b")  


# if else condition
if a > b:
    print("a is greater than b")
else:
    print("a is lesser than b")


# if else if condition
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
elif a < b:
    print("a is lesser than b")


print("=====================")

"""

marks_persentage is 95 and above  => A+
marks_persentage is 85 and above  => A
marks_persentage is 75 and above  => B+
marks_persentage is 65 and above  => B
marks_persentage is 55 and above  => C+
marks_persentage is 45 and above  => C
marks_persentage is 35 and above  => Passed

"""
marks_persentage = 53


if marks_persentage >= 95:
    print("Grade is : A+")
if marks_persentage >= 85 and marks_persentage < 95:
    print("Grade is : A") 
if marks_persentage >= 75 and marks_persentage < 85:
    print("Grade is : B+")
if marks_persentage >= 65 and marks_persentage < 75:
    print("Grade is : B")   
if marks_persentage >= 55 and marks_persentage < 65:
    print("Grade is : C+")
if marks_persentage >= 45 and marks_persentage < 55:
    print("Grade is : C")
if marks_persentage >= 35 and marks_persentage < 45:
    print("Grade is : Passed")


print("=====================")


num = 16

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is zero")

print("=====================")
