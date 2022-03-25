#1 Create a Person class and Employee Subclass. Person class has a name and age fields.
#  The Employee has a salary, position fields.
#  Define getter and setter functions for the fields.


class Person:
    def __init__(self, name, age ):
        self.name = name
        self.age = age

# class Employe(Person):
#     def __init__(self, name, age, salary, position):
#         super().__init__(name, age)
#         self.salary = salary
#         self.position = position


#2 Create a class and subclass. Create a calculate function in the class with two number arguments.
#  The function multiplicates 2 arguments.
#  Override the function in the subclass, which will multiply the values of the two arguments and divide the result to 2.

class Calc:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Divide(Calc):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def multiplicate(self):
        mult = self.x * self.y
        div = mult / 2
        print(div)

d = Divide(5,8)
d.multiplicate()



#3 Create a function to find the Fibonacci number.

# def Fibonacci(n):
   
#     if n < 0:
#         print("input largest number than 0 ")
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)

# print(Fibonacci(1))

#4 Create a file and write on it the input information (using input() function).

# input_text = input("input someone ")
# file_ = open('exx.txt', 'w')
# file_.write(input_text)

#5 Create two functions. The first one will concatenate 2 texts and the second one will remove white spaces from the text.
#  Create an uppercase text decorator and use it for the functions.

# def calc(text1, text2):


#6 Create a class, which allows creating only one instance

# class Car:
#     def __init__(self, manufacturer, year, color):
#         self.manufacturer = manufacturer
#         self.year = year
#         self.color = color

#     def print_car_details(self):
#         car_details = self.manufacturer + " " + str(self.year) + " " + self.color
#         print(car_details)

# car = Car('Subaru', 2012, 'green')
# car.print_car_details()

