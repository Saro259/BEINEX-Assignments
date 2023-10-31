# Write a Python program to multiplies all the items in a list.
def multiply(num_list):
    m = 1
    for i in num_list:
        m*=i
    return m

n = int(input("Enter the size of list"))
num_list = []
for i in range(0,n):
    ele = int(input())
    num_list.append(ele)
print(multiply(num_list))

# Write a Python program to remove duplicates from a list
def duplicates():
    final_list = []
    for n in num_list:
        if n not in final_list:
            final_list.append(n)
    return final_list
n = int(input("Enter the size of list"))
num_list = []
for i in range(0,n):
    ele = int(input())
    num_list.append(ele)
print(duplicates(num_list))

'''Write a Python program to count the number of strings where the string length is 2 or more.
	Sample List : ['abc', 'xyz', 'aba', '1']
	Expected Result : 3'''
def count():
    ct = 0
    for i in str_list:
        if len(i) >= 2:
            ct+=1
    return ct
str_list = []
for s in str_list:
    ele = input()
    str_list.append(ele)
print(count(str_list))

'''Write a Python program to print the numbers of a specified listafter removing even numbers from it
	list = [24,34,53,65,78,93,23,42]'''
def even_remove(num_list):
    for n in num_list:
        if n%2==0:
            num_list.remove(n)
    return num_list
num_list = [24,34,53,65,78,93,23,42]
print(even_remove(num_list))

'''Use list comprehension to contruct a new list but add 6 to each item.
	list = [24,34,54,45]'''
def add(num_list):
    new_list=[]
    for n in num_list:
        n+=6
        new_list.append(n)
    return new_list
num_list = [24,34,54,45]
print(add(num_list))

'''Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]'''
def squares(lst1):
    num_list=[]
    for n in lst1:
        if n > 50:
            num_list.append(n)
    return num_list
lst1=[2, 4, 6, 8, 10, 12, 14]
lst1 = [i**2 for i in lst1]
print(lst1)
print(squares(lst1))

# Write a Python program to find the repeated items of a tuple.
from collections import Counter

user_input= input("Enter space-seperated integers:")
tup = tuple(i for i in user_input.split()) 
for k,v in Counter(tup).items():
    if v > 1:
        print(f"{k} Repeated: {v}")