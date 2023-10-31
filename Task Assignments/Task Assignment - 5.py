# Write a Python function that calculates the factorial of a given integer. Demonstrate how to call this function with an example.

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

n = 14
print(f"Factorial of {n} is:", factorial(n))

# Create a function that takes two arguments, a name and an age, and prints a message like "Hello, [Name]! You are [Age] years old." Call this function with your name and age as arguments.

def introduction(name, age):
    print("Hello,"+name+"!"+"You are"+age+"years old.")
name = input("Enter your name")
age = input("Enter your age")
introduction(name,age)

# Write a Python function to find the maximum of three numbers.

def maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    elif c>b and c>a:
        return c
    else:
        return a
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
print("The largest number is:",maximum(a,b,c))

# Write a Python program to reverse a string

def reverse(str):
    str = str[::-1]
    return str
s = input("Enter a string")
print(reverse(s))

# Write a Python function that accepts a string and counts the number of upper and lower case letters.
def count(str):
    lower_case=0
    upper_case=0
    for i in str:
        if (i.islower()):
            lower_case+=1
        elif (i.isupper()):
            upper_case+=1
    return(lower_case,upper_case)
s = input("Enter a string consist of uppercase and lowercase alphabets")
lower_case, upper_case = count(s)
print("Number of lowercase alphabets are:",lower_case)
print("Number of uppercase alphabets are:",upper_case)

# Write a Python function that takes a number as a parameter and checks whether the number is prime or not. 

def prime_number(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if num%i==0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

n = int(input("Enter a number to find whether it is a prime number or not"))
prime_number(n)

''' Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow'''

def arrange_colors(s):
    li_str = list(s.split("-"))
    li_str.sort()
    return ('-'.join(li_str))
s = "green-red-yellow-black-white"
print(arrange_colors(s))

# Define a function that accepts 2 values and return its sum, subtraction and multiplication. Using 4 types of functions based on arguments and return type.

def sum(a,b):
    return a+b
def subtraction(a,b):
    if a>b:
        return a-b
    else:
        return b-a
def multiplication(a,b):
    return a*b
num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))
op = input("Enter the choice of operation +,-,*")
if op=='+':
    print("The sum is",sum(num1,num2))
if op=='-':
    print("The difference is",subtraction(num1,num2))
if op=='*':
    print("The product is",multiplication(num1,num2))


# Define a function that accepts roll number and returns whether the student is present or absent.

def student_attnd(roll_no):
    roll_list = [26,24,55,72,36]
    if roll_no in roll_list:
        print("Present")
    else:
        print("Absent")
roll_no = int(input("Enter your roll number"))
student_attnd(roll_no)

# Define a function that accepts lowercase words and returns uppercase words.

def to_uppercase(str):
    if str.islower():
        return str.upper()
s = input("Enter a string in lowercase")
print(to_uppercase(s))