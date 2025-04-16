# loops in python
# loops are use to repeat instructions
'''
# while loop
# repeat instructions as long as the condition is true
i = 0
while i < 500:
    print(i)
    i += 1
    # output: 0, 1, 2, 3, 4

# print numbers 1 to 100
i=1
while i<=100:
    print(i)
    i += 1

# print multiplication table of a number n.
n = 5
i = 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1

# print the elements of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]
numbers = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1




# break and continue statements
# break statement: terminate the loop

nums =(1,4,3,2,6,8,0,9)
x= 2;
i =0;
while i < len(nums):
    if nums[i] == x:
        print('found at ' ,i)
        break
    else:
        print("finding")
        i += 1
        print("loop ended")




# continue statement: skip the current iteration and move to the next one
# example
# print numbers 1 to 10, but skip 5
i=0
while i<= 5:
   if(i == 3):
       i+=1
       continue
   print(i)
   i += 1



        
# for loop in python
# for loop is used to iterate over a sequence (such as a list, tuple, dictionary,
# set, or string) or other iterable objects (such as files or generators)
# syntax: for variable in iterable:
# example: print numbers 1 to 10

for i in range (1,11):
    print(i)

# print the elements of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]
# using for loop

numbers =[1,4,9,16,25,36 ,64,81,100,49]
x= 49
i = 0
for item in numbers:
    if(item == x):
        print('found at idx',i)
        break
    i+=1


#range ()function
# returns a sequence of numbers starting from the first argument up to but not including the second argument

#range (start ,stop,step)
# start: the starting number of the sequence
# stop: the end of the sequence
# step: the difference between each number in the sequence
# example

seq =range (5)#range(stop)
for i in seq:
    print(i)

for i in range (2,10): #range(start ,stop)
    print(i)

for i in range (1,100,2): #range (start ,stop ,diff) #odd num
    print(i)

for i in range(2,100,2):#even num
    print(i)

    #practice questionn
    # print the numbers from 1 to hundread
for i in range(1,101):
    print(i)
    
for i in range(100,0,-1):
    print(i)
    
# multiplication table

n = int(input("Ente a number:"))

for i in range(1,11):
    print(n*i);

    
#pass statement 
# pass statement is used when we want to do nothing in a loop or in a function
# it is used as a placeholder when a statement is required syntactically but no execution of code
# is necessary

for i in range(1,11):
    pass
print("do some work")

if(i>5):
    pass
print("do some work")


#Wap to find the sum of first n numbers 


n =10
sum =0
for i in range(1,n+1):
    sum +=i

print("total sum " ,sum)
'''
#WAP to find the factorial of first n numbers .
n = 5
factorial = 1
for i in range(1,n+1):
    factorial *= i

print("factorial of " ,n,"is" ,factorial)
'''

 













    




