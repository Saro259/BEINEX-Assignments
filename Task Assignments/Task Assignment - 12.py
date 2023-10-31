'''Create a class named Student with name, score as instance attributes. 
Assign values to both of these attributes using a constructor.
Create 2 Student objects. And also define a method called 'display' in the Student class - 
which, when called should print the name and score of the student.'''

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def display(self, name, score):
        print(name)
        print(score)

std1 = Student('Saro Elza Mathew', 98)
std2 = Student('John Doe', 82)
std1.display(std1.name, std1.score)
std2.display(std2.name, std2.score)

'''Extend the above solution and add another instance attribute called grade (should be string). 
Assign value to grade from within the constructor.
The value should not be taken from user input.
Instead use the following conditions and assign values to grade by using the value of score.
grade = A+ if score >=90
grade = A if score >=80 and <90
grade = B+ if score >=70 and <80
and so on.
if score is below 40 then grade should be "FAILED" '''
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
        if self.score >=90:
            self.grade = 'A+'
        elif self.score>=80 and self.score<90:
            self.grade = 'A'
        elif self.score>=70 and self.score<80:
            self.grade = 'B+'
        elif self.score>=60 and self.score<70:
            self.grade = 'B'
        elif self.score>=50 and self.score<60:
            self.grade = 'C'
        elif self.score>=40 and self.score<50:
            self.grade = 'D'
        elif self.score<40:
            self.grade = 'FAILED'

    def display(self, name, score):
        print(f" Name: {name}")
        print(f" Score: {score}")
        print(f" Grade: {self.grade}")

std1 = Student('Saro Elza Mathew', 98)
std2 = Student('John Doe', 82)
std1.display(std1.name, std1.score)
std2.display(std2.name, std2.score)

'''Extend the above solution again and add an instance method named 'get_ehs' (short for eligible for higher studies) It should return a boolean. Return True if score is 40 and above.
Modify the 'display' method to include this EHS status also while printing.'''
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
        if self.score >=90:
            self.grade = 'A+'
        elif self.score>=80 and self.score<90:
            self.grade = 'A'
        elif self.score>=70 and self.score<80:
            self.grade = 'B+'
        elif self.score>=60 and self.score<70:
            self.grade = 'B'
        elif self.score>=50 and self.score<60:
            self.grade = 'C'
        elif self.score>=40 and self.score<50:
            self.grade = 'D'
        elif self.score<40:
            self.grade = 'FAILED'

    def get_ehs(self, score):
        if score>=40:
            return True
        else:
            return False
            
    def display(self, name, score):
        print(f" Name: {name}")
        print(f" Score: {score}")
        print(f" Grade: {self.grade}")
        print(" EHS", self.get_ehs(score))

std1 = Student('Saro Elza Mathew', 98)
std2 = Student('John Doe', 30)

print("Student info")
std1.display(std1.name, std1.score)
std2.display(std2.name, std2.score)

'''Extend the above solution again and add another instance method called 'as_dict'. 
The method should return a dictionary with the data of the student. 
It should contain 'name', 'score', 'grade', 'ehs_status' keys and their respective values.
Create Student 2 objects and call each of its methods.'''
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
        if self.score >=90:
            self.grade = 'A+'
        elif self.score>=80 and self.score<90:
            self.grade = 'A'
        elif self.score>=70 and self.score<80:
            self.grade = 'B+'
        elif self.score>=60 and self.score<70:
            self.grade = 'B'
        elif self.score>=50 and self.score<60:
            self.grade = 'C'
        elif self.score>=40 and self.score<50:
            self.grade = 'D'
        elif self.score<40:
            self.grade = 'FAILED'

    def get_ehs(self, score):
        if score>=40:
            return True
        else:
            return False
            
    def display(self, name, score):
        print(f" Name: {name}")
        print(f" Score: {score}")
        print(f" Grade: {self.grade}")
        print(" EHS", self.get_ehs(score))

    def display_dict(self, name, score):
        return {
            'Name': name,
            'Score': score,
            'Grade': self.grade,
            'EHS': self.get_ehs(score)
        }


std1 = Student('Saro Elza Mathew', 98)
std2 = Student('John Doe', 30)

print("Student info")
std1.display(std1.name, std1.score)
std2.display(std2.name, std2.score)

print("Display in dictionary:")
std1_dict = std1.display_dict(std1.name, std1.score)
std2_dict = std2.display_dict(std1.name, std2.score)
print(std1_dict)
print(std2_dict)