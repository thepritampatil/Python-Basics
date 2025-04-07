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
'''
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

















