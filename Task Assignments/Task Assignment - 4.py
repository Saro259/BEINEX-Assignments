# Python program to print all even/odd numbers in the range given by user
r = int(input("Enter the range uptil you need even/odd numbers"))
even = []
odd = []
for i in range(r):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("List of Even numbers")
print(*even)
print("List of Odd numbers")
print(*odd)

# Python program to print the multiplication table of any number (number should be taken as input and user decides the end limit of the table)
num = int(input("Enter the number whoose multiplication table to be displayed"))
r = int(input("Enter the limit of the table"))
for i in range(1,r+1):
    print(num*i)

# Find the factorial of a number taken as input using for loop
num = int(input("Enter the number to find the factorial"))
res = 1
for i in range(2,num+1):
    res*=i
print(res)

# Find the factorial of a number taken as input using while loop
num = int(input("Enter the number to find the factorial"))
res=1
while num>=2:
    res*=num
    num-=1
print(res)

# Find the sum of all even numbers between the range given by user
r = int(input("Enter the range uptil you need the sum of even numbers"))
sum = 0
for i in range(r+1):
    if i%2==0:
        sum+=i
print(sum)   

# Find the sum of all odd numbers between the range given by user using while loop
r = int(input("Enter the range uptil you need the sum of even numbers"))
sum = 0
while r>=0:
    if r%2!=0:
        sum+=r
print(r)

# Print first 10 fibonacci numbers using 'for' and 'while' loops

#for loop
n = 10
num1 = 0
num2 = 1
print(num1,num2,end=" ")
for i in range(2, n):
    num3 = num2+num1
    print(num3, end=" ")
    num1 = num2
    num2 = num3

# while loop
n = 10
num1 = 0
num2 = 1
c= 0 
print(num1,num2,end=" ")
while c <n-2:
    num3 = num1+num2
    print(num3, end=" ")
    num1 = num2
    num2 = num3
    c+=1

    



''' print the following patterns
(a)
	    	*
           * *
          * * *
         * * * *

(b)		o
		1 2
		3 4 5
		6 7 8 9


(c)		o
		1 1
		2 2 2
		3 3 3 3

(d)		*
		* *
		* * *
		* * * *'''

#a
row = 4
for i in range(row+1):
    for j in range(row-i):
        print(' ',end="")
    for k in range(2*i-1):
        print('*', end=" ")
    print("")

#b
row = 4
current_num = 0
for i in range(row+1):
    for j in range(0,i):
        print(current_num,end="")
        current_num+=1
    print("")

#c
row = 4
for i in range(row):
    for j in range(0,i+1):
        print(i, end=" ")
    print("")

#d
row=4
for i in range(row+1):
    for j in range(i):
        print("*",end=" ")
    print("")

