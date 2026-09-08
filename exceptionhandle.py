# Exception Handling

#try...except statement
try:
    result = 10 / 0    # Attempting to divide 10 by 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")


a = 1
try:
    b = int(input("Please enter a number to divide a: "))
    a = a / b    #Python的基礎數字型態在除以零時不會傳回NaN，而是直接拋出ZeroDivisionError。
    print("Success a =", a)
except:
    print("There was an error")
