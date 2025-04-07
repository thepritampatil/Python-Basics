#string in python
#string is a datatype that stores a sequence of character
"""
# basic opertion in string 
# 1. indexing
example
name = "Rahul"
print(name[3]) # prints u
# 2. slicing
example
name = "Rahul"
print(name[1:4]) # prints ahu
#backword counting using slicing
example
name = "Rahul"
print(name[-1]) # prints l
# 3. concatenation
example
name = "Rahul"
print(name + "Sharma") # prints RahulSharma
# 4. repetition
example
name = "Rahul"
print(name * 3) # prints RahulRahulRahul
# 5. length
example
name = "Rahul"
print(len(name)) # prints 5
# 6. lower and upper case
example
name = "Rahul"
print(name.lower()) # prints rahul
print(name.upper()) # prints RAHUL
# 7. split and join
example
name = "RahulSharma"
print(name.split(" ")) # prints ['Rahul', 'Sharma']
print(name.join())
# 8. replace
example
name = "RahulSharma"
print(name.replace("Rahul", "Rohan")) # prints RohanSharma
# 9. strip
example
name = "   Rahul   "
print(name.strip()) # prints Rahul
# 10. count
example
name = "RahulSharma"
print(name.count("R")) # prints 2
# 11. startswith and endswith
example
name = "RahulSharma"
print(name.startswith("R")) # prints True
print(name.endswith("a")) # prints False
# 12. find and rfind
example
name = "RahulSharma"
print(name.find("R")) # prints 0
#13 capitalize
example
name = "rahulsharma"
print(name.capitalize()) # prints Rahulsharma (first letter capital)

#14 casefold
example
name = "RAHULSHARMA"
print(name.casefold()) # prints rahulsharma
#15 zfill
example
name = "123"
print(name.zfill(5)) # prints 00123

"""
#wap to input user's first name & print its length
name = input("Enter your first name: ")
print(len(name))
# 2. wap to find occurrece of '$' in a String
name = input("Enter your name: ")
print(name.count('$'))


















