# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.
def add(n):
    return lambda n: n+15
num = 10
print(add(num))

def multiply(x):
    return lambda y: x*y
t = multiply(7)
num = 7
print(t(num))

# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def multiply(x):
    return lambda x: x*5
x = 2
print(multiply(x))

# Write a Python program to find if a given string starts with a given character using Lambda
check = lambda x, char : x.startswith(char)

ip_char = "H"
x = "Hash brown"
result = check(x, ip_char)
if result:
    print("The string starts with H")
else:
    print("The string does not start with H")

# Write a Python program to extract year, month, date and time using Lambda.
import datetime
year = lambda x: x.year
month = lambda x:x.month
day = lambda x:x.day
time = lambda x:x.time()

x = datetime.datetime.now()
print(year(x)) 
print(month(x))
print(day(x))
print(time(x))

# write a python program to check whether a given string is a number or not using lambda
num_check = lambda x: x.isdigit()
str = "1234"
res = num_check(str)
if res:
    print("It is a number")
else:
    print("It is not a number")

'''Write a Python program to create Fibonacci series up to n using Lambda.
Fibonacci series upto 2:
[0, 1]
Fibonacci series upto 5:
[0, 1, 1, 2, 3]
Fibonacci series upto 6:
[0, 1, 1, 2, 3, 5]'''
from functools import reduce

fib = lambda n: reduce(lambda x, _:x+[x[-1]+x[-2]],range(n-2),[0,1])

print(fib(6))

# Write a Python program to find palindromes in a given list of strings using Lambda.
str_list = ["php", "malayalam", "abcd", "aaaa"]
reverse = list(filter(lambda x: (x=="".join(reversed(x))),str_list))
print(reverse)

# Write a Python program that multiplies each number in a list with a given number using lambda functions. Print the results.
num_list = [2,3,4,16]
multiply = lambda num_list, number: [x * number for x in num_list]
number = 2
print(multiply(num_list, number))

# Write a Python program to find the maximum value in a given heterogeneous list using lambda
hetro_list = ['Python', 3, 2, 4, 5, 'version']
maximum = max(hetro_list, key = lambda i: (isinstance(i, (int, float), i)))
print(maximum(hetro_list))

# Create a Python module (a separate .py file) that contains a function to calculate the area of a rectangle. Then, in another Python script, import the module and use the function to calculate the area of a rectangle with specific dimensions.
import rectangle_area
length = float(input("Enter the length of the rectangle"))
breadth = float(input("Enter the breadth of the rectangle"))
print(rectangle_area.area(length, breadth))