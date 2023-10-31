"""Task 1
======

1) Create a class named Shape. Add an instance method called area. But don't define the method, just raise NotImplementedError() exception with a suitable message.

2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC)
Make the area method an abstract method by decorating it with abstractmethod decorator (import this also from abc).

3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
Define custructor for each of them to assign the necessary parameters required for calculating the area.
Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it.

Create an object for each of the subclasses and call the area method on the objects."""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area():
        raise NotImplementedError("Suitable user inputs only allowed")


class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return float(0.5 * self.height * self.base)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return float(self.side**2)


class Pentagon(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return float((5 / 4) * self.side**2 / (math.tan(math.pi / 5)))


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return float(math.pi * (self.radius**2))


triangle = Triangle(3, 6)
print("The area of the triangle is :", triangle.area())

square = Square(4)
print("The area os square is :", square.area())

pentagon = Pentagon(5)
print("The area of pentagon is :", pentagon.area())

circle = Circle(12)
print("The area of circle is :", circle.area())

'''Task 2
======

Create a class named Cypher. The purpose of that class is to receive an input string of charecters and convert it to another cypher string. Use a constructor to receive the input. (Dont use user input by using input() function, pass the value as static)

The class must have a class method to do the string convertion. And an instance method to invoke the classmethod from within it.
Use the below convertion logic:
- Iterate over each chanrector in the string, and if the charector is a digit increment it by one (0->1, 1->2, ... 9 should be replaced with 0)
- if the charector is an alphabet then shift the charector by 2 positions (use chr() and ord() builtins for this) (a->c, b->d, ... y->a, z->b) If the charector is in upper case convert it to lower and vice versa
- The returned string must be of same length as the input.

No need to implement the reversing algorithm, but will be a plus if available

1) create an object for the Cypher class with the string.
2) call the instance method, which should internally call the classmethod you prepared for the convertion, pass the string data to classmethod and do the convertion.

No need to consider special charecters for now.

Expected output for the string "ABcD1293Z" is "cdEf2304b"'''


class Cypher:
    def __init__(self, cypherInput):
        self.cypherInput = cypherInput

    @classmethod
    def cypher_text(self, cypherInput):
        res = []
        for ch in cypherInput:
            if ch.isdigit():
                if ch == 9:
                    ch = (int(ch) + 1) % 10
                    res.append(str(ch))
                else:
                    ch = int(ch) + 1
                    res.append(str(ch))
            elif ch.isalpha():
                if ch.isupper():
                    ch = chr(((ord(ch) - ord("A") + 2) % 26) + ord("A"))
                    res.append(ch.lower())
                if ch.islower():
                    ch = chr(((ord(ch) - ord("a") + 2) % 26) + ord("a"))
                    res.append(ch.upper())
            else:
                res.append(ch)
        return "".join(res)

    def cypher_conversion(self):
        return self.cypher_text(self.cypherInput)


cypher = Cypher("ABcD1293Z")
print("The Cyphered text is:", cypher.cypher_conversion())
