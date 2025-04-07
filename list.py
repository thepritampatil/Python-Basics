#List in python
#List is a collection of items which can be of any data type including strings, integers, float
#List is ordered and changeable. It allows duplicate values.
#List is denoted by square brackets [] and elements are separated by comma.
#List is mutable, which means it can be modified after it is created.
#List is a collection which is ordered and changeable. It allows duplicate values.  

# it can store elements of different types (integer ,float string)
'''
# example

marks=[43.2,45.4,67,75,90,63.6]
print(marks);
student =["pritam",22,90.56]
print(student);
student[0]="Pratik"
print(student);


#List slicing
#List slicing is a process of extracting a subset of elements from a list.
#It is done using the colon(:) operator.
#The syntax for list slicing is: list[start:stop:step] where start is the starting
# index, stop is the ending index and step is the increment between elements.
#If start is omitted, it is considered as 0. If stop is omitted, it is
# considered as the last index. If step is omitted, it is considered as 1.
#Example
marks=[43.2,45.4,67,75,90,63.6]
print(marks[1:4]);#prints 45.4 67 75
print(marks[:4]);#prints 43.2 45.4 67 75
print(marks[2:]);#prints 67 75 90 63.6
print(marks[:]);#prints 43.2 45.4 67 75
print(marks[-3:-1]);#75 90

#List methods
#List methods are functions that can be used to perform various operations on lists.
#Some of the common list methods are:
#append() : This method adds an element to the end of the list.
#extend() : This method adds multiple elements to the end of the list.
#insert() : This method inserts an element at a specified position in the list.
#remove() : This method removes the first occurrence of an element in the list.
#pop() : This method removes and returns an element at a specified position in the list.
#index() : This method returns the index of the first occurrence of an element in the list.
#count() : This method returns the number of occurrences of an element in the list.
#sort() : This method sorts the elements of the list in ascending order.
#reverse() : This method reverses the order of the elements in the list.
#Example
marks=[43.2,45.4,67,75,90,63.6]
print(marks)
#append() method
marks.append(78)
print(marks)
#extend() method
marks.extend([89,90,91])
print(marks)
#insert() method
marks.insert(2,85)
print(marks)
#remove() method
marks.remove(90)
print(marks)
#sort() method
marks.sort()
print(marks)


#Tuples in python
#Tuples are similar to lists but are immutable, i.e., they cannot be changed after they are created. Tuples are defined by enclosing a sequence of values in parentheses.

#Tuples are immutable, so you cannot change their elements 
# a?fter they are created.
#If you try to change a tuple, you will get an error.
#Tuples are faster than lists because they are immutable, so Python can optimize them better.
#Tuples are also more memory efficient than lists because they do not have the overhead of the list
#Example
marks=(43.2,45.4,67,75,90,63.9)
print(marks)
print(type(marks))


#tupple methods
#index
#count
#Example
marks=(43.2,45.4,67,75,90,63.9,67,90,67)
print(marks.index(67))
print(marks.count(67))


#WAP to ask the user to enter names of their 3 favorite movies & store in a list
movies =[]
movi1=input("Enter first movie:")
movi2=input("Enter second movie:")
movi3=input("Enter third movie:")

movies.append(movi1)
movies.append(movi2)
movies.append(movi3)
print(movies)
print(type(movies))

#WAP to check if a list contains a palindrome of elements (use copy method)
list1 = [1, 2, 3, 2, 1]
list2 = [1, 3, 4, 4, 5]

copy_list1 =list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")

'''


#WAP to count the number of students with the "A" grade in the following tuple.
# ["C","D","A","A","B","B","A"]

grade = ["C","D","A","A","B","B","A"]
grade.sort()
count = grade.count("A")
print(count)










 



