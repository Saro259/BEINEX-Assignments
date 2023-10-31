# write a single program to handle the following arithmetic operations for addition, subtraction, multiplication , division, floor division,modulus and Exponentiation.

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

'''0
   0 0
   0 0 0
   0 0 0 0'''

for i in range(5):
    for j in range(i):
        print("0",end=" ")
    print("")

'''     *
      * * *
    * * * * *
  * * * * * * *'''
row = 4
for i in range(row+1):
    for j in range(row-i):
        print('  ',end="")
    for k in range(2*i-1):
        print('*',end=" ")
    print("")

''' 0
    1 1
    2 2 2
    3 3 3 3
    4 4 4 4 4
    5 5 5 5 5 5'''

for i in range(6):
    for j in range(0,i+1):
        print(i, end="")
    print("")

''' 1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5'''

for i in range(6):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")

'''* * * * * *
    * * * * *
    * * * *
    * * * 
    * *
    *'''

for i in range(7):
    for j in range(6,i,-1):
        print('*',end=" ")
    print("")

'''@ @ @ @ @ @ @

   @ @ @ @ @ @ @

   @ @ @ @ @ @ @

   @ @ @ @ @ @ @'''

for i in range(5):
    for j in range(7):
        print("@", end=" ")
    print("")

'''Write a program to check the validity of a password. Primary conditions for password validation:
	- minimum 8 charecters
	- The alphabet must be between [a-z]
	- At least one alphabet should be of Upper Case [A-Z]
	- At least 1 number or digit between [0-9].
	- At least 1 character from [ _ or @ or $ ].'''

str = "Rama1_fortune$"  
u = 0
l = 0
c = 0
d = 0
if (len(str))>= 8:
    for w in str:

        if w.isupper():
            u+=1
        if w.islower():
            l+=1
        if w.isdigit():
            d+=1
        if w=='@' or w=='$' or w=='_':
            c+=1
if u>=1 and l>=1 and d>=1 and c>=1 and l+u+d+c==len(str):
    print("valid password")
else:
    print("Invalid Password")

