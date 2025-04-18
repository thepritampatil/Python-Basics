# what is OOP in  python

# OOP is a programming paradigm that uses objects and classes to design applications and programs.
# It is a way of writing code that is easy to read, write, and maintain.
# OOP is based on the concept of objects, which are instances of classes, and classes,
# which are blueprints for creating objects.

# OOP in Python is based on the following four principles:

# 1. Encapsulation: 
# This is the idea of bundling data and methods that operate on that data within a single unit, called a class.

# 2. Inheritance: 
# this is the idea of creating a new class based on an existing class, inheriting its attributes and methods.

# 3. Polymorphism:
#  This is the idea of having multiple forms of a method or operator, depending on the context in which it is used.

# 4. Abstraction: 
# This is the idea of showing only the necessary information to the outside world, while hiding the implementation details.


#Class and Objects in python
# A class is a blueprint or a template that defines the properties and behavior of an object.

# An object is an instance of a class and has its own set of attributes (data) and
'''
#creating class
class Student:
     name ="karan"
     age =21

s1 =Student()  #creating objects(instance)
s2 =Student()
print(s1.name) 
print(s1.age)
print(s2.name)
print(s2.age)

class Car:
     color ="blue"
     brand= "mercedes"


     # creating objects(instance)
car1 =Car()
car2 =Car()
print(car1.brand)
print(car1.color)


#_init_() function use
# Constructor
#all classes have a function called _init_(),which always executed when the object is being initiated

#default constructor
class Student:
     def __init__(self):
          pass
     
    #  PArameterized construtor
class Student:
     def __init__(self,name,age,marks):#parameterized construtors
          self.name = name
          self.age = age
          self.marks =marks
          #creating objects(instance)

s1 =Student("pritam",21,90) 
s2 =Student("prathmesh",20,50)
print(s1.name)
print(s1.age)
print(s1.marks)
print(s2.name)
print(s2.age)
print(s2.marks)


#the self parameter is a reference to the current instance of the class and is used to access variables



#class & instance attribute

class Student:
     # class attribute
     college = "KL"

     def __init__(self,name,marks):
          # instance attribute
          self.name = name
          self.marks = marks
          #creating objects(instance)

s1 =Student("pritam",90)
s2 =Student("prathmesh",50)
print(s1.college) #accessing class attribute
print(s2.college) #accessing class attribute
print(s1.name) #accessing instance attribute
print(s1.marks) #accessing instance attribute
print(s2.name) #accessing instance attribute
print(s2.marks) #accessing instance attribute


#Methods 
#Methods are functions that are defined inside a class.
#Methods are used to perform some specific task.
#Methods are used to access and modify the attributes of a class.

# creating class 
class Student:
     def __init__(self,name,marks):
          self.name = name
          self.marks = marks

     def welcome(self):
          print("welcome to the class",self.name)
     def get_marks(self):
          return self.marks
     
          #creating objects(instance)
s1 =Student("pritam",90)
s1.welcome()
s2 =Student("prathmesh",50)

#accessing attributes using methods 

print(s1.name) #accessing attribute using method
print(s1.get_marks())
print(s2.name) #accessing attribute using method
print(s2.marks) #accessing attribute using method



#let's practice

# create student class that takes name & marks of 3 subjects as arguments in a constructor. Then create a method to print the average

class Students:
     def __init__(self, name, marks):
          self.name = name
          self.marks = marks
     def get_avg(self):
        sum = 0
        for val in self.marks:
             sum += val

        print("hi ", self.name, "your avg score is ", sum/3)

s1 =Students("Iron man",[99,98,95])
s1.get_avg()

#Static Methods 

#Static methods are methods that belongs to a class rather than an instance of the class.

# Static methods are used to perform some specific task.

# Static methods are used to access and modify the attributes of a class.

class Student:
     @staticmethod # decorator
     def college():
          print("MIT")

s1.Student()



#Abstraction in python
#Abstraction is a concept of object-oriented programming that refers to the practice of hiding the implementation details of an object from the user and showing only the necessary information to the user.
#Abstraction is used to reduce complexity and improve the security of a system.
#Abstraction is used to improve the performance of a system.
#Abstraction is used to improve the maintainability of a system.

#Abstraction is used to improve the scalability of a system.
#Abstraction is used to improve the reusability of a system.
#Abstraction is used to improve the flexibility of a system.
#Abstraction is used to improve the portability of a system.
#Abstraction is used to improve the security of a system.

#  Example
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch =False


    def start(self): 
        self.clutch =True #abstraction (not necessory details are hide)
        self.acc = True
        print("car started")

car1 =Car()
car1.start()
    
#Encapsulation

#Encapsulation is the concept of bundling data and methods that operate on that data within a single unit, called a class or object.

#Encapsulation is used to hide the implementation details of an object from the user and show only the necessary information to the user.

# Create Account class with 2 attribute - balance & account no Create method for debit ,credit & printing the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no =acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs",amount ,"was debited")
        print("total balance =",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs",amount ,"was credited")
        print("total balance =",self.get_balance())

    def get_balance(self):
        return self.balance
    


acc1 = Account(10000,2321)
acc1.get_balance()
acc1.credit(51000)
acc1.debit(1000)
acc1.credit(5000)



#Del keyword
#del keyword is used to delete properties or object itself.

# del.s1.name

class Student:
    def __init__(self, name):
        self.name = name
    

s1= Student("pritam")
del s1
print(s1)


   

#private(like) Attributes and methods

#Private attributes and methods are not directly accessible from outside the class. They are used to hide the implementation details of a class from the outside world.

#Private attributes are declared by prefixing them with double underscore(__) and private methods are declared by prefixing them with double underscore(__) and they are called as mangled attribute names.

class Account:
    def __init__(self, accno, name, acc_pass):
        self.__accno = accno
        self.__name = name
        self.__acc_pass = acc_pass
    def reset_pass(self):
    print(self.__acc_pass)
    

acc1 =Account("12345","abcde")
print(acc1.__accno)
print(acc1.__acc_pass)


#Inheritance

#Inheritance is a process where one class can inherit the properties and methods of another class. 
# The class that is being inherited is called the parent class or superclass and the class that is doing the inheriting is called the child class or subclass.
#Inheritance is used to create a new class that is a modified version of an existing class.

# example
class Car :
    @staticmethod
    def car_start():
        return "Car is started"
    @staticmethod
    def car_stop():
        return "Car is stopped"
    
class ToyotaCar(Car):
    def _init_(self,name):
     self.name = name

car1 =ToyotaCar("fortuner")
car2 =ToyotaCar("prius")
print(car1.car_start())
print(car2.car_stop())

#types of innheritance
#1.Single Inheritance
#Single level inheritance is a type of inheritance where a child class inherits the properties and methods of a single parent class.
# example
class Animal:
   def __init__(self, name, age):
      self.name = name
      self.age = age

def eat(self):
   print(self.name + " is eating")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

     #  creating objects
dog1 = Animal("Bella", 3 )
dog2 = Dog("Max", 2,"poddle" )
print(dog1.name)
print(dog2.name)
print(dog2.breed)

#class method
# A class method is bound to the class & receive the class as an implicit first argument
# class method is used to create a class from a class
# note - Static method can't access or modify class state & generally for utility


#  example
class Person:
    name = 'anonymous'
    def changeName(self,name):
        self.name = name
        @classmethod
        def changeName(cls,name):
            cls.name = name
            
person1 = Person()
person1.changeName("John")
print(person1.name)  

#property method
#property method is used to get and set the value of a variable
#property method is used to create a property of a class    
#example
class Student :
    def __init__(self, phy, chem, math):
        self._phy = phy
        self._chem = chem
        self._math = math
        
        
    @property
    def percentage(self):
       return str((self._phy + self._chem +self._math)/3)+"%"
        

stu1 = Student( 98, 97, 99)
print(stu1.percentage)

stu1._phy =70
print(stu1.percentage)


# polymorphism : Operator Overloading 
# operator overloading is a feature of object oriented programming that allows us to redefine the behavior of operators 
#when the same operator is allowed to have diffrent meaning according to the context
# example
class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real ,"i" ,"+",self.img,"j")

    def addNum(self, num2):
        newReal= self.real +num2.real
        newImg = self.img + num2.img
        return ComplexNumber(newReal, newImg)
    
   

num1 =ComplexNumber(1,3)
num1.showNum()
num2 =ComplexNumber(4,6)
num2.showNum()

num3 =num1.addNum(num2)
num3.showNum()


#Dunder functions
#dunder functions are special functions in python that are used to overload operators
# example
class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
         print(self.real ,"i" ,"+",self.img,"j")
    def __add__(self, num2):
         newReal= self.real +num2.real
         newImg = self.img + num2.img
         return ComplexNumber(newReal, newImg)
        
    def __sub__(self ,num2):
        newReal= self.real -num2.real
        newImg = self.img - num2.img
        return ComplexNumber(newReal, newImg)
        
num1 =ComplexNumber(1,3)
num1.showNum()
num2 =ComplexNumber(4,9)
num2.showNum()

num3 =num1 + num2
num4 =num2 - num1

num3.showNum()
num4.showNum()




#let's Practice

#Q Define a Circle class to create a circle with radius r using the constructor . Define a area method of the class which calculates the area of the circle .
# Define a perimeter () method of the class which allows you to calculate  the perimeter of the circle

class Circle :
    def __init__(self,radius):
        self.radius = radius
    def area (self):
        return 22/7 * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * 22/7 * self.radius 
    
c1 =Circle(34)
print(c1.area())
print(c1.perimeter())


#Q2 Define a employee class with attribute role ,department & salary .This class  shwoDetail() method
#create an Engineer class that inherites properties from Employee & 


class Employee :
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print("role =",self.role)
        print("department =",self.department)
        print("salary =",self.salary)

class Engineer(Employee):
    def __init__(self, name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","4000000")

        

Eng1 =Engineer("Pritam Patil", 22)
Eng1.showDetails()

E1 =Employee("Accountant","Finance", "15000")
E1.showDetails()


'''
# Q3 Create a class called Order which stores item & its prices
#Use Dunder function __gt__() to convey that 
#order> order 2 if price of order > price of order2 

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self,odr2): #gt - greater than
        return self.price > odr2.price
    
odr1 = Order("chips",100)
odr2 = Order("burger",20)
print(odr1>odr2)







    
        
        
    


          
          







