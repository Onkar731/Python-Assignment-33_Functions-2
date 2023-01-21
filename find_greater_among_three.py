"""
Write a python function to find greater among three numbers (TSRS)
"""

# defining a function "find_greater()" which takes three numbers as an argument
# and returns greater number among three 
def find_greater(num1, num2, num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3:
        return num2
    else:
        return num3
    
# taking input from the user
num1, num2, num3 = int(input("Enter three numbers : ")), int(input()), int(input())

# printing greater number
print("Greater is", find_greater(num1, num2, num3))