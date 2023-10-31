""" Create a class Employee with name and salary attributes.

The salary has to be calculated and should be initialized to zero.
Create a method to calculate the salary by taking the no of hours worked and multiply it by 200.
You can give no of hours to the method as an argument.

Now create a child class ParttimeEmployee by inheriting the Employee class,
and by using method overriding (create salary calculation method in this class also with the same name)
get the salary of part time employee by multiplyig no of hours worked by 150.

Create 3 objects for each class.
Now implement '+' operator overloading and
find the total salary expense for keeping those employees by adding up the objects together."""


class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id
        self.emp_salary = 0

    def cal_salary(self, hours_of_work):
        self.emp_salary = hours_of_work * 200

    def __add__(self, other):
        total_emp = Employee(self.emp_id + other.emp_id)
        total_emp.emp_salary = self.emp_salary + other.emp_salary
        return total_emp


class Parttime_Employee(Employee):
    def cal_salary(self, hours_of_work):
        self.emp_salary = hours_of_work * 150

    def __add__(self, other):
        total_parttimeemp = Parttime_Employee(self.emp_id + other.emp_id)
        total_parttimeemp.emp_salary = self.emp_salary + other.emp_salary
        return total_parttimeemp


emp1 = Employee(101)
emp1.cal_salary(40)

emp2 = Parttime_Employee(21)
emp2.cal_salary(16)

emp3 = Employee(112)
emp3.cal_salary(45)

total_expense = emp1 + emp2 + emp3
print(total_expense.emp_salary)

#or

class Employee:
    salary_multiplier = 200

    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def update_salary(self, hours):
        self.salary = hours * self.salary_multiplier

    def __add__(self, other):
        return self.salary + other

    def __radd__(self, other):
        return self.salary + other


class PartTimeEmployee(Employee):
    salary_multiplier = 150


e1 = Employee(name="John")
e1.update_salary(hours=10)

e2 = Employee("Dev")
e2.update_salary(hours=10)

e3 = PartTimeEmployee("Naveen")
e3.update_salary(hours=5)

e4 = PartTimeEmployee("Lia")
e4.update_salary(hours=5)

total_expense = e1 + e2 + e3 + e4
print("Total Expense:", total_expense)