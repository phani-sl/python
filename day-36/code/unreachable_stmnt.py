# After return
def my_function():
    print("Start")
    return "Done"
    print("This will never run")  # Unreachable
    # The second print() after return will never execute because the function exits at return.

result = my_function()
print(result)

# After raise
def check_age(age):
    if age < 18:
        raise ValueError("Too young!")
        print("This line is unreachable")  # Unreachable
    print("Access granted.")
    # Once raise executes, the exception interrupts the flow and the next statement never runs.

check_age(15)


# After break
for i in range(5):
    print(i)
    break
    print("This will never print")  # Unreachable # output 0
    # break ends the loop immediately, so the following statement is unreachable

# After continue
for i in range(3):
    continue
    print("Unreachable in loop")  # Unreachable
# continue skips directly to the next loop iteration, so the print() is never executed.