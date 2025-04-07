print("hello","pritam");
print("world");
print(23+23);


''' multiline comments
 in python '''
 # variable in python

#variable is name given to a memory location in program
# variable can be of any data type like int, float, string, boolean etc.
# variable name should be a valid python identifier
# variable name should not be a keyword in python
# variable name should not start with a number
# variable name should not contain any special character except underscore
# variable name should be a single word,meaningful short,simple

name = "pritam" #string
age = 23 #int 
price = 25.44 #floating value
is_adult = True #boolean
print("my name is :" ,name);
print("my age is :" ,age);
print("my price is :" ,price);
print("am i adult:" ,is_adult);

print(type(name))
print(type(age))
print(type(price))
print(type(is_adult))

#DataTypes in python
#1. Integers ( +ve ,-ve , 23 -23 ,0)
#2. Float ( decimal values 93.34)
#3. boolean ( true ,false)
#4. String  ( name = "sk" ,name2 ='sk' ,name3='''sk'')
#5. NoneType 

age = 34
old =True
a = None
print(type(age));
print(type(old));
print(type(a));

#Keywords in python
#1. and    
#2. as
#3. assert
#4. async
#5. await
#6. break
#7. class
#8. continue
#9. def
#10. del
#11. elif
#12. else
#13. except
#14. finally
#15. for
#16. from
#17. global
#18. if
#19. import
#20. in
#21. is
#22. lambda
#23. nonlocal
#24. not
#25. or
#26. pass
#27. raise
#28. return
#29. try
#30. while
#31. with
#32. yield

#pritn sum
a=2333
b=543
sum=a+b
diff=a-b
multi=a*b
divi=a/b
print(sum ,diff,multi,divi);

#Types of tokesn in python
#1. punctuators
# are symbols to organize senttence structure in programming 
# (),{},@,# etc

#Epression Execution in python

# String & Numeric values can operate together with *
# A,B=2,3
#Txt ="@"
#print(2*Txt*3)
# output @@@@@@ ( when string multiply with numeric value  string will repeat ntime)


# String & String values can operate together with +
# A,B="2",3
#Txt="@"
# print(A+Txt)*B) --("2"+"@")3
#output 2@2@2@  ( concatenate)

#Numeric value can operate with all arithmatic operators
#A,B=2,3
# C=4
# print(A+B*C)  -- 2+3*4
#output 14

#Arithmatic expression with Integer and float will result in float
#A,B=2,3.0
# print(A*B)  -- 2*3.0
#output 6.0

#Result of division operator with two integers will be float
#A,B=2,3
# print(A/B)  -- 2/3
#output 0.6666666666666666

#interger division with float and int will give int displayed as float
#A,B=2,3.0
#C=A//B
# print(C,A/B)  -- 2//3.0
#output (0.0, 0.6666666666666666)

#floor gives closet Integer ,which is lesser than or equal to the float value
# result of (A//B )is same as floor (A/B)
#A,B=12,5
#C=A//B
# print(C)  -- 2
#output 2

#A,B=12,5
#C=A//B
# print(C)  -- -3
#output -3

#Remiander is negative when denominator is negative
#A,B=5,2
#C=A%B
# print(C)  -- 1
#output 1

#A,B=-5,2
#C=A%B
# print(C)  -- 1
#output 1

#A,B=5,-2
#C=A%B
# print(C)  -- -1
#output -1

#comments in python
"""comments are use to 
#explain the code
# comments are ignored by python interpreter
"""
#single line comments
""" this 
is multiline
comment  """
# print("Hello")  #this is a comment

#Input in python
"""
#input() function is used to get input from user

#String input
#taking input from user & printing it
name=input("Enter your name:")
print(name)

#int input
#taking input from user & printing it
age=int(input("Enter your age:"))
print(age)

#float input
#taking input from user & printing it
price=float(input("Price of my shoe:"))

print("My Name is " ,name ,"and I am ",age, "years old. My shoe price is",price)

"""

