"""Write a Python program that prompts the user to enter an integer and handles the ValueError exception 
if the user enters a non-integer value."""


def get_integer():
    try:
        v = int(input("Enter a numeric value"))
        print(f"The numeric value is {v}")
    except ValueError:
        print("Invalid value, Please enter an integer")


get_integer()


"""Create a program that opens a file and reads its contents. 
Use a try-except block to handle the FileNotFoundError exception and 
display a custom error message if the file does not exist."""


def file_open():
    try:
        f = open("POEM.txt")
        line = f.read()
        print(line)
        f.close()
    except FileNotFoundError:
        print("The file you are trying to open does not exists.")


file_open()


""" Write a program that calculates the division of two numbers entered by the user. 
Use a try-except block to handle the ZeroDivisionError exception and 
display an appropriate error message if the user tries to divide by zero."""


def division(a, b):
    try:
        res = a / b
        print("Result is:", res)
    except ZeroDivisionError:
        print("The division by zero is not valid")


a = 20
b = 0
division(a, b)


"""Create a program that attempts to connect to a website and prints the HTML content if successful. 
Use a try-except-else block to handle the requests.exceptions.
RequestException exception and display an error message if the connection fails."""

import requests

try:
    response = requests.get("https://www.example.com")
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("An error occurred", e)
else:
    print("Request Successful !")


"""Write a program that opens a file, reads its contents, and writes the contents to a new file.
Use a try-except-finally block to ensure that the file is closed even if an exception occurs during the file operations."""


def file_write():
    try:
        f2 = open("New.txt", "w")
        f = open("POEM.txt")
        line = f.read()
        f2.write(line)
    except FileNotFoundError:
        print("The file you are trying to open to write does not exist")
    finally:
        f2 = open("new.txt", 'r')
        line = f2.read()
        print(line)
        f2.close()
        f.close()


file_write()

""" Write a Python program that reads email details (sender, recipient, subject, and body) from user input and 
sends the email using Mailtrap as the SMTP server."""

import smtplib
from email.mime.text import MIMEText

email_sender = "saroelzamathew.com"
email_receiver = "receiverend.com"
subject = "Testing mail for production"
body = "I am sending this test mail for checking the server. Please Ignore"

message = MIMEText(body)
message["From"] = email_sender
message["To"] = email_receiver
message["Subject"] = subject

smtp_server = "sandbox.smtp.mailtrap.io"
smtp_user = "92fc1b9814a0fc"
smtp_pass = "e1e070cb14d9a8"
smtp_port = "2525"

server = smtplib.SMTP(smtp_server, smtp_port)
print("---server---", server)

server.starttls()
server.login(smtp_user, smtp_pass)
server.sendmail(email_sender, email_receiver, message.as_string())

print("-----Email Sent------")
server.quit()

# write a python program to send an email with multiple recipients using the smtplib library.

import smtplib
from email.mime.text import MIMEText

email_sender = "saroelzamathew.com"
email_receiver = ["receiverend.com", "receiver.com", "tester.com"]
subject = "Testing mail for production"
body = "I am sending this test mail for checking the server. Please Ignore"

message = MIMEText(body)
message["From"] = email_sender
message["To"] = ",".join(email_receiver)
message["Subject"] = subject

smtp_server = "sandbox.smtp.mailtrap.io"
smtp_user = "92fc1b9814a0fc"
smtp_pass = "e1e070cb14d9a8"
smtp_port = "2525"

server = smtplib.SMTP(smtp_server, smtp_port)
print("---server---", server)

server.starttls()
server.login(smtp_user, smtp_pass)
server.sendmail(email_sender, email_receiver, message.as_string())

print("-----Email Sent------")
server.quit()


# write a python program to handle exceptions when sending emails using Python's smtplib library.

import smtplib
from email.mime.text import MIMEText
from smtplib import *

email_sender = "saroelzamathew.com"
email_receiver = ["receiverend.com", "receiver.com", "tester.com"]
subject = "Testing mail for production"
body = "I am sending this test mail for checking the server. Please Ignore"

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    print("---server---", server)

    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(email_sender, email_receiver, message.as_string())

except SMTPResponseException as e:
    error_code = e.smtp_code
    error_message = e.smtp_error

    print("Error code:" + error_code)
    print("Message:" + error_message)

'''Write a Python program that prompts the user to enter their age. 
Define a custom exception called InvalidAgeError that is raised when the entered age is less than 0 or greater than 150. 
Handle the InvalidAgeError exception and display an appropriate error message.'''

class InvalidAgeException(Exception):
    pass

def age_input():
    try:
        input_num = int(input("Enter a number:"))
        if input_num >150 or input_num <0:
            raise InvalidAgeException
        else:
            print("Your age is", input_num)

    except InvalidAgeException:
        print("Age input is invalid !")

age_input()

'''Write a Python program that simulates a banking system. 
Implement a class called BankAccount with methods to initialize an account with a starting balance, withdraw funds, 
and handle a custom exception called NegativeBalanceError when the account balance goes below zero.'''

class NegativeBalanceError():
    pass
    def __init__(self, starting_balance, message = "Invalid starting balance"):
        self.starting_balance = starting_balance
        self.message = message
        #super().__init__(self.message)

class BankAccount():

    def __init__(self, starting_balance, withdraw_funds):
        self.starting_balance = starting_balance
        self.withdraw_funds = withdraw_funds

starting_balance = int(input("Enter your opening balance"))
if starting_balance < 0:
    raise NegativeBalanceError(starting_balance)

