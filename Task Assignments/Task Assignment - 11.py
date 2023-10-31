# Write a function to return even numbers from a list
'''def even_number(num_list):
    even_list=[]
    for n in num_list:
        if n%2==0:
            even_list.append(n)
    return even_list

s = int(input("Enter the size of the list"))
num_list = []
print("Enter the list of numbers:")
for i in range(0,s):
    ele = int(input())
    num_list.append(ele)
print("The list of even numbers are:\n",even_number(num_list))'''

# Write a function to find the largest item from a given list
def largest(num_list):
    return max(num_list)

s = int(input("Enter the size of the list"))
num_list = []
print("Enter the list of numbers:")
for i in range(0,s):
    ele = int(input())
    num_list.append(ele)
print("The largest item in the list",largest(num_list))

'''Write a Python function that takes a list and returns a new list with unique elements of the first list
	Sample List : [1,2,3,3,3,3,4,5]
	Unique List : [1, 2, 3, 4, 5]'''
'''def distinct(num_list):
    num_list = list(set(num_list))
    return num_list

s = int(input("Enter the size of the list"))
num_list=[]
print("Enter the list of numbers:")
for i in range(0,s):
    ele = int(input())
    num_list.append(ele)
print("Distinct list of numbers:\n",distinct(num_list))'''

'''Write a Python function to multiply all the numbers in a list
	Sample List: (8, 2, 3, -1, 7)
	Expected Output: -336'''
'''def multiply(num_list):
    m = 1
    for n in num_list:
        m*= n
    return m

num_list = [8,2,3,-1,7]
print("Multiplied answer is:\n",multiply(num_list))'''

# Python Program to find sum of digit of number using recursion.
'''def sum_digits(num):
    if num ==0:
        return 0
    return (num%10 + sum_digits(int(num/10)))
num = int(input("Enter a more than one digits number"))
print("Sum of digits: \n",sum_digits(num))'''

# Python Program to add two number using recursion.
def add(num1, num2):
    if num2 ==0:
        return num1
    return add(num1,num2 - 1) + 1
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
print("Sum of two inputs are:\n",add(n1,n2))

# Python Program to merge two arrays.
s1 =int(input("Enter the size of list"))
s2 = int(input("Enter the size of list"))
num_list1 = []
num_list2 = []
print("Enter the list of numbers:")
for i in range(s1):
    ele = int(input())
    num_list1.append(ele)
print("Enter the list of numbers:")
for j in range(s2):
    ele = int(input())
    num_list2.append(ele)
merge_list = num_list1 + num_list2
print("New merge list is", merge_list)

# Python program to perform right rotation in array by 2 positions.
s = int(input("Enter the size of list"))
print("Enter the list of numbers:")
num_list = []
for i in range(s):
    ele = int(input())
    num_list.append(ele)
for i in range(0,2):
    temp = num_list[s-1]
    for j in range(s-1, -1, -1):
        num_list[j]= num_list[j-1]

    num_list[0]=temp
print("Array after rotations:\n", num_list)

# Python Program to print all odd numbers in array
s = int(input("Enter the size of list"))
num_list = []
print("Enter the list of numbers:")
for i in range(s):
    ele = int(input())
    num_list.append(ele)
print("Odd numbers are")
for i in num_list:
    if i%2!=0:
        print(i)

# Python Program to find sum of array elements.
s = int(input("Enter the size of list"))
arr=[]
sum=0
print("Enter the list of numbers:")
for i in range(s):
    ele = int(input())
    arr.append(ele)
for i in arr:
    sum+=i
print("Sum of all numbers is:\n",sum)

# Python Program to delete element from array at given index
s = int(input("Enter the size of list"))
arr=[]
sum=0
print("Enter the list of numbers:")
for i in range(s):
    ele = int(input())
    arr.append(ele)
index = int(input("Enter the index of the element to be removed"))
del arr[index]
print("New array is:\n",arr)

# Python Program to calculate length of an array.
arr = [12,23,45, 60, 9]
print("Length of array:\n", len(arr))

# Python program to reverse an Array in two ways.
arr = [12,23,45, 60, 9]
l = len(arr)
for i in range(l//2):
    arr[i], arr[l-i-1] = arr[l-i-1], arr[i]
print("Reversed array:\n", arr)

#another way
import array as arr
arr = [12,23,45, 60, 9]
arr.reverse()
print("The reversed array is:\n", arr)

