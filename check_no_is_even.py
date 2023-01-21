"""
Write a python function to check if a number is even (TSRS)
"""

# defining a function "is_even()" which takes a number as an argument
# and returns True or False 
def is_even(num):
    return True if num&1 != 1 else False

# taking input from the user
num = int(input("Enter a number : "))

# printing whether the given number is even
print(is_even(num))