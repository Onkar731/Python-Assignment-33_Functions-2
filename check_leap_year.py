"""
Write a python function to check if a year is leap year (TSRS)
"""

# defining a function "is_leap_year()" which takes a year as an argument
# and returns True or False
def is_leap_year(year):
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        return True
    else:
        return False
    

# taking input from the user
year = int(input("Enter a year : "))

# printing year is leap year or not
print("%d is a leap year" %(year) if is_leap_year(year) else "%d is not a leap year" %(year))