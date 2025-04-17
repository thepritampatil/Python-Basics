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
'''

#_init_() function use
# Constructor
#all classes have a function called _init_(),which always executed when the object is being initiated

class Student:
     def __init__(self,name,age):
          self.name = name
          self.age = age
          #creating objects(instance)

s1 =Student("pritam",21)
print(s1.name)
print(s1.age)

