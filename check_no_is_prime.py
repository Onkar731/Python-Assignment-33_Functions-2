"""
Write a python function to check whether a number is prime (TSRS)
"""

# defining a function "is_prime()" which takes a number as an argument
# and returns True or False
def is_prime(num):
    i = 2
    while i<num:
        if num%2 == 0:
            return False
        i += 1
    
    if i == num:
        return True
    

# taking input from the user
num = int(input("Enter a number : "))

# printing whether the number is prime or not
print("%d is a prime number" %(num) if is_prime(num) else "%d is not a prime number" %(num))