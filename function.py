#What is Functions in python
#Functions are blocks of code that can be reused multiple times in a program.
#They can take arguments and return values.
#Functions are defined using the def keyword.
#Functions can be used to perform a specific task, such as calculating the area of a rectangle or   
#displaying a message on the screen.
#Functions can also be used to organize code and make it easier to read and understand.
# two types of functions
#1. built-in functions
#2. user-defined functions
# built-in functions
#1. print()
#2. len()
#3. type()
#4. range()
#5. max()
#6. min()
#7. sum()
#8. str()
#9. int()
#10. float()
# user-defined functions
#1. def function_name():
#2. def function_name(parameters):

'''
# example
# function defination
def cal_sum(a,b):#parameters
    sum =a+b
    print(sum)
    return sum #return statement

cal_sum(4,2)
cal_sum(-10,4289)#function call ; arguments

#In this example, the function cal_sum takes two arguments, a and b, adds them together

#and prints the result. The function also returns the result, which is then printed by the function

# average of 3 numbers

def average(a,b,c):
    avg=(a+b+c)/3
    return avg

#function call
print(average(10,20,30))#arguments



def cal_prod(a=1,b=1):
    product = a * b
    return product

print(cal_prod())
print(cal_prod(5,6))#function call; arguments

#Wap to print the length of a list .(list is the parameter)

cities =["delhi","gurugram","pune","Banglore","chennai","hyderabad"]
heros =["shaktiman","hanuman","iron man","spiderman"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heros)

#Waf to print the elements of a list in a single line.(list is the parameter)
def print_elements(list):
    for item in list:
        print(item,end="")

print_elements(cities)
print_elements(heros)

# Waf to find the factorial of n.(n is the parameter)
def find_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    print(fact)

find_fact(5)
'''


# Waf to convert INR to USD
def converter(usd_val):
    inr_val = usd_val * 83.23
    return inr_val
print(converter(100))








