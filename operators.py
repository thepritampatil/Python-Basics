#Operators
# an operater is an symbol that perform a certain operation between operands
"""
#types of operators in python

#1. Arithmetic operators
a=5
b=3
print(a+b)  
print(a-b)
print(a*b)
print(a/b)
print(a%b)  # modulus operator
print(a**b)  # exponentiation operator
print(a//b)  # floor division operator
"""

#2. relational/Comparison operators(==,!=,>,<,>=,<=)
"""
a =50
b=20
print(a==b)  # equality operator
print(a!=b)  # not equal operator
print(a>b)  # greater than operator
print(a<b)  # less than operator
print(a>=b)  # greater than or equal to operator
print(a<=b)  # less than or equal to operator


#4. Assignment operators
num=10;
num += 10;
num -= 10;
num *= 10;
num /= 10;
print(num)

#5. Logical operators

# not operator
a =20;
b=30;
print(not False);
print(not True);
print(not(a<b))



# and operator
val1 =True;
val2=False;
print(val1 and val2);
print(val1 and val2==False);

#or operator
val1 =True;
val2=False;
print(val1 or val2);
print(val1 or val2==True);
print(val1 or val2==False);


#type conversion in python
#It refers to automatically changing a value from one data type to another by the compiler or interpreter.
#python has built in functions to convert data types
#1.int() function is used to convert a number or a string into an integer
#2.float() function is used to convert a number or a string into a floating point number
#3.str() function is used to convert a number or a string into a string
#4.complex() function is used to convert a number or a string into a complex number
#5.bin() function is used to convert a number into a binary number
#6.hex() function is used to convert a number into a hexadecimal number
#7.oct() function is used to convert a number into an octal number
#8.list() function is used to convert a string into a list
#9.tuple() function is used to convert a list into a tuple
print(int(10.5))  #converting float to int
print(float(10))  #converting int to float
print(str(10))  #converting int to string
print(complex(10))  #converting int to complex number
print(bin(10))  #converting int to binary number
print(hex(10))  #converting int to hexadecimal number
print(oct(10))  #converting int to octal number

"""
#type casting in python

# It refers to explicitly changing a value from one data type to another by the programmer.

#python has built in functions to convert data types
#1.int() function is used to convert a number or a string into an integer
#2.float() function is used to convert a number or a string into a floating point number
#3.str() function is used to convert a number or a string into a string
#4.complex() function is used to convert a number or a string into a complex number
#5.bin() function is used to convert a number into a binary number
#6.hex() function is used to convert a number into a hexadecimal number
#7.oct() function is used to convert a number into an octal number
print(int("10"))  #converting string to int
print(float("10.5"))  #converting string to float
print(str(10))  #converting int to string
print(complex("10"))  #converting string to complex number
print(bin(10))  #converting int to binary number
print(hex(10))  #converting int to hexadecimal number
print(oct(10))  #converting int to octal number

#difference between type casting an type conversion























