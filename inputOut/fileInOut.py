
# open() function
# open() function is used to open a file. It returns a file object, which has methods
'''
f= open("D:\Python\inputOut\demo.txt","w")
f.write("Hello, world!")
f.close();

# read()
# read() function is used to read the content of a file. It returns a string containing the
# contents of the file.
f = open("D:\Python\inputOut\demo.txt", "r")
print(f.read())
f.close()


# readlines()
# readlines() function is used to read all lines in a file and return them as a list
# of strings. Each line in the file is a separate element in the list and the lines are
# separated by newline characters.
f = open("D:\Python\inputOut\demo.txt", "r")
print(f.readlines())
f.close()

# readline()
# readline() function is used to read a line from a file. It returns a string containing
# the line at the current position in the file. The line is read from the current position
# in the file to the end of the line. The line is then moved to the next line
f = open("D:\Python\inputOut\demo.txt", "r")


line1= f.readline()
print(line1)

line2 =f.readline()
print(line2)

f.close()

#writing to a file
# write() 
f = open("D:\Python\inputOut\demo.txt", "a")

f.write ("I want to learn MERN Stack\n")
f.write("first I moved to react js")
f.close()

# modes
# 'r' - read mode
# 'w' - write mode
# 'a' - append mode
# 'r+' - read and write mode
# 'a+' - append and read mode
# 'x' - create mode
# 'b' - binary mode
# 't' - text mode
# '+' - open a disk file for updating(reading and writing)

# with use
# with open() function is used to open a file. It is used to open a file and
# automatically close the file when the block of code is exited. It is used to
# avoid memory leak and to prevent the file from being left open after the
  
# with open() as variable_name

with open("D:\Python\inputOut\demo.txt","r") as f:
    data = f.read()
    print(data)

with open("D:\Python\inputOut\demo.txt","w")as f:
    f.write("new data")

# Deleting a file (using os module)
#import os
# os.remove() function is used to delete a file. It is used to delete a file from the file system.

import os
os.remove("D:\Python\inputOut\sample.txt")


#Let's practice

# Create a new file "practice.txt" using python. Add the following data in it

# Hi everyone 
# we are learning File I/O
# using Java
# I like programming in Java

#WAF that replace all occurence of "java "with python in above file

with open("D:\Python\inputOut\practice.txt","r") as f:
    data = f.read()
    data = data.replace("java", "Python")   

with open("D:\Python\inputOut\practice.txt","w" ) as f:
    f.write(data)

#Search if the "learning" exists in file or not
def check_for_word():
    with open("D:\Python\inputOut\practice.txt","r") as f:
     data = f.read()
     word ="learning"
    if (data.find(word)!= -1):
        print("word exists in file")
    else:
        print("word does not exist in file")

    
check_for_word()


#WAF to find i which line of the file does the word "learning" occur first.

def check_for_line():
     word ="in"
     data =True
     line_no=1
     with open("D:\Python\inputOut\practice.txt","r") as f:
          while data:
               data = f.readline()
               if word in data: 
                    print(line_no)
                    line_no +=1
     return -1

check_for_line()
'''
#




        

    



      



     
        
        

    


