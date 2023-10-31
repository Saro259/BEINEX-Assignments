# Implement a program that reads a text file and counts the occurrences of each word, ignoring case sensitivity.

d = dict()
f = open("text.txt", 'r')
line = f.read()
chars = line.split()
for i in chars:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k in list(d.keys()):
    print(k, ":", d[k])

''' Write a Python function that takes a list of strings as input and returns a new list with
the strings sorted in descending order of their lengths.'''

def sorted():
    print("Enter word strings")
    for s in range(size):
        ele = input()
        string_list.append(ele)
    sorted_list = sorted(string_list, key=lambda x: len(x))
    return(sorted_list)
size = int(input("Enter the size of list"))
string_list = []
print(sorted(string_list))

# Write a function that takes a list of numbers as input and returns the second-largest number.

def second_largest(num_list, n):
    num_list.sort()
    return num_list[n-2]

n = int(input("Enter the size of the list"))
num_list=[]
for i in range(n):
    ele = int(input())
    num_list.append(ele)
print(second_largest(num_list,n))

# Write a Python program that takes a list of integers as input and returns a new list with only the numbers that are prime.

def prime(num_list):
    prime_list = []
    for i in num_list:
        if i > 1:
            for p in range(2,i):
                if (i%p) ==0:
                    break
            else:
                prime_list.append(i)
    return prime_list
n = int(input("Enter the size of the list"))
num_list=[]
for i in range(n):
    ele = int(input())
    num_list.append(ele)
print("The numbers from the list which are only prime are:",prime(num_list))

# Write a Python function that takes a list of integers as input and returns a new list with only the numbers that are perfect squares.

import math 

def perfect_squares(num_list):
    perfect_list = []
    perfect_list.append([k for k in num_list if (math.sqrt(k)==math.floor(math.sqrt(k)))])
    return perfect_list

num_list = [10, 4, 5, 35, 16, 80, 36, 25, 40, 81, 49, 90, 200, 100]
print("The perfect squares are:", perfect_squares(num_list))

# Write a Python function that takes a list of numbers as input and returns the sum of all the numbers divisible by 3 or 5.

def sum_of_divisible(num_list):
    sum = 0
    for i in num_list:
        if i%3==0 or i%5==0:
            sum+=i
    return sum
n = int(input("Enter the size of the list"))
num_list=[]
for i in range(n):
    ele = int(input())
    num_list.append(ele)
print("The sum of numbers which are divisible by 3 or 5 is",sum_of_divisible(num_list))

'''Write a Python function called calculate_discounted_price that takes the original
price of an item and a discount percentage as input. The function should return the
discounted price after applying the discount. Ensure that the function handles the
case where the discount percentage is negative and raises a custom exception
called InvalidDiscountError with an appropriate error message.'''

class InvalidDiscountError(Exception):
    pass

def calculate_discounted_price(price, disc_percent):
    try:
        if disc_percent < 0:
            raise InvalidDiscountError
        else:
            price_after_discount = float(price - ((disc_percent/100)*price))
            print(price_after_discount)

    except InvalidDiscountError:
        print("discount percent is invalid !")

price = int(input("Enter the price of the item you have purchased:"))
disc_percent = int(input("Enter the discount percent to be deducted from the price:"))
calculate_discounted_price(price, disc_percent)

'''Write a function that takes a sentence as input and returns a new sentence with the words reversed,
while keeping the order of the words in the sentence.'''
def reverse_words(s):
    reverse = []
    spl_str = s.split()
    for i in spl_str:
        reverse.append(i[::-1])
    return(" ".join(reverse))

s = "The sun set behind the mountains painting the sky in shades of orange and purple."
print(reverse_words(s))

'''Implement a program that simulates a basic calculator, allowing users to perform
arithmetic operations (addition, subtraction, multiplication, division) on two numbers.'''

def calculator(f_num,s_num,op):
    if op=='+':
        return(first_num+second_num)
    if op=='-':
        if first_num > second_num:
            return(first_num - second_num)
        else:
            return(second_num - first_num)
    if op=='*':
        return(first_num * second_num)
    if op=='/':
        return(first_num / second_num)
    if op=='%':
        return(first_num % second_num)
    if op=='**':
        return(first_num ** second_num)
    if op=='//':
        return(first_num // second_num)

first_num = int(input("Enter a number"))
second_num = int(input("Enter another number"))
op = input("Enter any operator (+,-,*,/,%,**,//):")
print("Your calculation:\n",calculator(first_num,second_num,op))

'''Create a class named Notes for handling text-based file operations.
Class should contain methods "write", "read" and then "append" as instance methods
or class methods. (Can contain any other methods if you wish)
Use a single file for saving the notes. You can set the file name as a constant
somewhere in the program (Or as a class variable).
write method should create the if it doesn't exist, Then it should overwrite the older
contents with the user input if the user plans to overwrite the file.
read method should read the whole file contents and return it. If the file doesn't exist,
then it should return "No notes found"
append method should take the user input value and it must add the value to the end
of the file. It must not overwrite the file.
Now create a program to utilize this class. The program should repeatedly ask the
user for these 4 choices :
1 - Write Note (Overwrite existing).
2 - Add more Notes (Append).
3 - Read Notes.
4 - Exit'''

class Notes:

    file_name = "Save.txt"

    def write(self, input):
        f = open(self.file_name, 'w')
        f.write(input + '\n')
        f.close()
        print("Notes successfully saved!")

    def read(self):
        try:
            f = open(self.file_name, 'r')
            line = f.read()
            return(line)
        except FileNotFoundError:
            print("The file you are trying to open does not exists.")


    def append(self, append_string):
        f = open(self.file_name, 'a')
        f.write(append_string)
        f.close()


    def menu(self):
        print("Menu \n 1 - Write Note (Overwrite existing).\n"
                            "2 - Add more Notes (Append).\n"
                            "3 - Read Notes.\n"
                            "4 - Exit")
        op_input = int(input("Enter the operation number you would like to choose"))

        if op_input==1:
            content_string = input("Enter Your notes:")
            self.write(content_string)
        elif op_input==2:
            append_string = input("Enter the string to be appended")
            self.append(append_string)
        elif op_input==3:
            note = self.read()
            print(note)
        elif op_input==4:
            print("Exit")
        else:
            print("Please put a valid input")
        
        self.menu()

notes = Notes()
notes.menu()

