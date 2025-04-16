#what is Recursion in python
#Recursion is a programming technique where a function calls itself in its own definition.
#Recursion is a powerful tool for solving problems that have a recursive structure, such as tree or
#graph traversals, or problems that can be broken down into smaller instances of the same problem.
#Recursion is a technique where a function calls itself in its own definition. It is a powerful
#tool for solving problems that have a recursive structure.
'''
#syntax
#def function_name(parameters):
#   function_name(parameters)  # recursive call
#   # function body
#Example of recursion in python
def show(n):
    if n == 0: #base case
     return
    print(n)
    show(n-1) #recursive call
show(5)


def fact(n):
   if (n == 0 or n==1): #base case
      return 1
   else:
      return n * fact(n-1) #recursive call
   
print(fact(5))  # Output: 120

#WARF to calculate the sum of first natural number
def sum_of_natural_numbers(n):
    if n == 1: #base case
        return 1
    else:
        return n + sum_of_natural_numbers(n-1) #recursive call
    
print(sum_of_natural_numbers(5))
'''
#WARF to print all elements in a list.(use list and idx as parameter)
def print_list(list, idx=0):
    if idx == len(list): # base case
        return
    print(list[idx])
    print_list(list, idx+1)
    
fruit=['mango','banana','litche','apple']
print(print_list(fruit))

    