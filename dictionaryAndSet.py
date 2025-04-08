# Dictionary in python 
# A dictionary is a collection of key-value pairs
# It is mutable, meaning it can be changed after it is created
# It is an unordered collection of key-value pairs  
# It is an associative array, meaning that each key is associated with a value
'''
# It is a data structure that stores data in the form of key-value pairs
# example
dict ={
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}
# Accessing values in a dictionary
print(dict["name"])  # Output: John
print(dict["age"])    # Output: 30
print(dict["city"])    # Output: New York
# Adding a new key-value pair to a dictionary   
dict["country"]="USA"
print(dict)  # Output: {'name': 'John', 'age': 30, 'city':New York ,'country':USA}  
# Updating a value in a dictionary
dict["age"]=31
print(dict)  # Output: {'name': 'John', 'age': 31, '
# Removing a key-value pair from a dictionary
del dict["city"]
print(dict)  # Output: {'name': 'John', 'age': 31, '
# Checking if a key exists in a dictionary
if "name" in dict:
    print("Key exists")  # Output: Key exists
else:
    print("Key does not exist")  # Output: Key does not exist

# Checking if a key exists in a dictionary using the get() method
print(dict.get("name"))  # Output: John
print(dict.get("fullname"))  # Output: None
# Checking if a key exists in a dictionary using the in operator
print("name" in dict)  # Output: True
print("fullname" in dict)  # Output: False

# Creating a dictionary from a list of key-value pairs
# example
dict = dict([("name", "John"), ("age", 30), ("city","USA")])
print(dict)  # Output: {'name': 'John', 'age': 30,'city

#create nested dictionary
dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "address": {
        "street": "123 Main St",
        "apartment": 4,
        "country": "USA"
    }
    "is_addult"= True;
}
# Accessing values in a nested dictionary
print(dict["address"]["street"])  # Output: 123 Main St
print(dict["address"]["apartment"])  # Output: 4

# Dictionary methods
# 1. clear() - Removes all items from the dictionary
dict.clear()
print(dict)  # Output: {}
# 2. copy() - Returns a copy of the dictionary
dict = {"name": "John", "age": 30}
dict_copy = dict.copy()
print(dict_copy)  # Output: {'name': 'John', 'age': 30}
# 3. fromkeys() - Creates a new dictionary with the specified keys and values
dict = {"name": "John", "age": 30}
dict_fromkeys = dict.fromkeys(["city", "country"], "USA")
print(dict_fromkeys)  # Output: {'city': 'USA', 'country': 'USA
# 4. get() - Returns the value for the specified key if it exists in the dictionary
print(dict.get("name"))  # Output: John
print(dict.get("fullname"))  # Output: None
# 5. items() - Returns a view object that displays a list of all key-value pairs
print(dict.items())  # Output: dict_items([('name', 'John'), ('age',
# 6. keys() - Returns a view object that displays a list of all keys
print(dict.keys())  # Output: dict_keys(['name', 'age'])
# values() returns all values
print(dict.values())  # Output: dict_values(['John', 30])
# update() insert the specified items to the dictionary
dict = {"name": "John", "age": 30}
dict.update({"city": "New York", "country": "USA"})
print(dict)  # Output: {'name': 'John', 'age': 30, '
# pop() removes the specified key-value pair from the dictionary
dict = {"name": "John", "age": 30}
print(dict.pop("age"))  # Output: 30
# popitem() removes the last inserted key-value pair from the dictionary


# ---------------------------------------------------

#Sets in python
# set is the collection of the unordered itemes.
# each element in the set is unique & immutable
set1 = {1, 2, 3, 4, 5,"pritam"}
collection = set() #empty set

print(set1);
print(type(set1)); #total no of items

#set methods
#1.add() - add the item to the set
set1 = {1, 2, 3, 4, 5}
set1.add(6)
print(set1)  # Output: {1, 2, 3, 4,
#2.clear() - removes all items from the set
set1 = {1, 2, 3, 4, 5}
set1.clear()
print(set1)  # Output: set()
#3.copy() - Returns a copy of the set
set1 = {1, 2, 3, 4, 5}
set1_copy = set1.copy()
print(set1_copy)  # Output: {1, 2, 3, 4,5}
#4.remove() - remove the element
set1 = {1, 2, 3, 4, 5}
set1.remove(3)
print(set1)  # Output: {1, 2, 4, 5}
#5.pop() - remove the random element from the set r
set1 = {1, 2, 3, 4, 5,"random"}
print(set1.pop())  # Output: 1
print(set1.pop())
#6.union() - #combines both set values & returns new
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) #{1,2,3,4,5,6,7,8}

#7.intersection() - returns the common values
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.intersection(set2)) #{4,5}


#Practice Questions
#store the following word meaning in a python dictionary
# table :"a piece of furnitur","list of faccts & figures"
# cat :"a small animal"

dictionary ={
    "cat": "a small animal",
    "table": ["a piece of furiture","list of facts & figures"]
}

print(dictionary)
print(type(dictionary))

#your are given a list of subjects for students .Assume one classroom is required for 1 subjects. How many clssroom are needed by all students

subjects = {
    "python","java","c++","python","javaScript","java",
    "python","java","c++","c"

}
print(subjects)
print(type(subjects))
print(len(subjects))

#wap to enter marks of 3 subjects from the user and store them in a dictionary .Start with an empty dictionary & add one by one.Use subject name as key & marks as value

marks = {}

x = int(input("enter phy"))
marks.update({"phy": x})
y = int(input("enter chem"))
marks.update({"chem": y})
z = int(input("enter math"))
marks.update({"math": z})   
print(marks)
'''
#figure out a way to store 9 & 9.0 a seprate values in the set .
values={9,"9.0"}
print(values)












