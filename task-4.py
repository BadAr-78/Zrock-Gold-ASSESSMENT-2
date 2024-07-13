''' Write a Python program that uses a try-except block to handle a division
by zero error.'''

num1 = 5
num2 = 0

try:
    result = num1 / num2
except ZeroDivisionError:
    result = 0
print(result)