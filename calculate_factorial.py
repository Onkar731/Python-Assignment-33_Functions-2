"""
Write a python function to calculate factorial of a number (TSRS)
"""

# defining a function "factorial()" which takes a number as an argument
# and returns the factorial of that number
def factorial(num):
    fact = 1
    for e in range(1, num+1):
        fact *= e
    return fact

# taking input from the user
num = int(input("Enter a number : "))

# printing factorial of the number
print("Factorial =", factorial(num))