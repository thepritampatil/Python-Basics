#Conditional in python
#Conditional statements are used to execute different blocks of code based on certain conditions.
#There are three types of conditional statements in python: if, elif, else.

#if-elif-else
#The if-elif-else statement is used to execute different blocks of code based on certain conditions
#The if statement is used to check if a condition is true or not. If the condition is
#true, the block of code inside the if statement is executed.
#The elif statement is used to check if a condition is true or not. If the condition is
#true, the block of code inside the elif statement is executed. If the condition is false,
#the next elif statement is checked and so on.

"""
light =input("light color:")

if (light=="red"):
    print("stop")
elif (light=="green"):
    print("go")
elif(light=="yellow"):
    print("slow down")
else:
     print("cautious")

     



#example 2

marks = int(input("marks:"))
if (marks >= 90 and marks < 100):
    print("A grade")
elif (marks >= 80 and marks < 90):
    print("B grade")
elif (marks >= 70 and marks < 80):
    print("C grade")
else:
    print("fail")

    """

# Single line / Ternary operators
#The ternary operator is a shorthand way of writing if-else statements in a single line.
#It is used to assign a value to a variable based on a condition.
"""

food = str(input("food :"))
eat = "yes" if food == "cake" else "no"
print(eat)
 
 #clever If / Ternary operator
 #The clever if is a shorthand way of writing if-else statements in a single line.
 #It is used to assign a value to a variable based on a condition.

 

age = int(input("age :"))
vote =("yes","no") [age < 18]
print(vote)
sal = float(input("salary :"))
tax = ("0.1","0.2") [sal <= 50000]
print(tax);



# Best practices
#1. Use meaningful variable names
#2. Use comments to explain the code
#3. Use functions to organize the code
#4. avoid complex expressions
#5. One instruction per task


# Wap to check if a number entered by the user is odd or even

num = int(input("Enter a number:"))
if (num%2==0) :
   print("Even")
else:
   print ("odd")
   

# Wap to find the greatest of three numbers entered by user.
a = int(input("enter a number:"))
b = int(input("enter b number:"))
c = int(input("enter c number:"))
if (a>=b) and (a>=c):
    print("a is the greatest")
elif(b>=c):
    print("b is the greatest")
else:
    print("c is the greatest")
"""


#wap to check if number is multiple of 7 or not
num = int(input("enter a number:"))
if (num%7==0):
    print("multiple of 7")
else:
    print("not a multiple of 7")
    





















