''' Write python programs , which accept two inputs and perform the following arithmetic operations
	i)    Addition (+)
        ii)   Subtraction (-)
        iii)  Multiplication (*)
        iv)   Division (/)
        v)    Modulus (%)
        vi)   Exponentiation (**)
        vii)  Floor Division (//) '''

first_num = int(input("Enter a number"))
second_num = int(input("Enter another number"))
op = input("Enter any operator (+,-,*,/,%,**,//):")

if op=='+':
    print(first_num+second_num)
if op=='-':
    if first_num > second_num:
        print(first_num - second_num)
    else:
        print(second_num - first_num)
if op=='*':
    print(first_num * second_num)
if op=='/':
    print(first_num / second_num)
if op=='%':
    print(first_num % second_num)
if op=='**':
    print(first_num ** second_num)
if op=='//':
    print(first_num // second_num)

'''Python Program to replicate bank transaction: min balance 500, ask user the amount to withdraw, 
     print the balance amount after withdrawal, if user enters an amount greater than balance: print:: insufficient balance. 
     if balance is below 500 print an alert message : your account balance is "available_balance", Please  keep your account balance above Rs.500 to avoid unwanted charges.'''

initial_cash = 1000
min_balance = 500
withdrawal_cash = int(input("Enter the amount to be withdrawn"))
if withdrawal_cash > min_balance:
    print("Insufficient balance")
bal = float(initial_cash) - float(withdrawal_cash)
if bal < min_balance:
    print(f"Your balance is {bal}, Please keep your account balance above Rs.500 to avoid unwanted charges")
else:
    print(f"Your balance is {bal}")

'''Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same'''

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))
max_num = max(a,b,c)
print(f"{max_num} is the greatest of all")

'''Python program to check the number taken as an input is even or odd,print invalide input if user enters anything other than integers'''

a = int(input("Enter a number"))
if a%2==0:
    print("It is an even number")
elif a%2!=0:
    print("It is an odd number")
else:
    print("Invalid Input")

'''Python program to check the score from a student ,print grades as A+ if score >= 90,A if 80 or above, B+ if 70 or above and so on... 
    print failed if the score is below 50, if score > 100 print invalid'''

student_marks = float(input("Enter your marks"))
if  student_marks >= 90 and student_marks<=100:
    print("You scored an A+")
elif student_marks >=80 and student_marks < 90:
    print("You scored A")
elif student_marks < 80 and student_marks >=70:
    print("You scored B+")
elif student_marks <70 and student_marks >=60:
    print("You scored B")
elif student_marks <60:
    print("You scored C")
else:
    print("Invalid Input")