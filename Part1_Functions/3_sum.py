# https://www.w3schools.com/python/python_casting.asp / https://www.w3schools.com/python/python_scope.asp
# Write a function add(a, b) that returns the sum of the two numbers.
# Ask the user for two numbers (as input), convert them to integers, call the function, and print the result.
    
# Write your code here:

def add(a,b):
    return a+b 
a=int(input("Type a number:"))
b=int(input("Type a second number"))

result=add(a,b)
print("Result:",result)