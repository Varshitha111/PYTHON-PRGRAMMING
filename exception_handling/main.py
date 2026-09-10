# Append to an existing file
#  Create notes.txt containing some text. 
# Take a new sentence from the user and append it to the existing file using "a" mode. 
# Then read and display the complete file.
with open("notes.txt","a") as file:
    file.write("I'm writing something new here")
with open("notes.txt","r") as file:
    content=file.read()
print(content)

# Append multiple lines
#  Create students.txt with 3 student names. 
# Ask the user for 2 additional names and 
# append them to the same file without deleting the existing names.
with open("students.txt","a") as file:
    for i in range(2):
        name=input("enter name")
        file.write(name+"\n")
with open("students.txt","r") as file:
    content=file.read()
print(content)
# Overwrite an existing file
#  Create a file containing some old information. 
# Ask the user for new information and use "w" mode to replace the old content completely. 
# Read the file afterward to verify the change.
with open("demo.txt","w") as file:
    content=input("enter the new content")
    file.write(content)
with open("demo.txt","r") as file:
    content=file.read()
print(content)
# Check whether a file exists
#  Ask the user for a filename. 
# Check whether the file exists before attempting to open it. 
# Display an appropriate message depending on whether the file exists or not.
import os
filename=input("enter file name")
if os.path.exists(filename):
    print("File Exists")
    with open(filename,"r") as file:
        content=file.read()
print(content)
# Delete a file
#  Ask the user for a filename and delete that file. 
# If the file doesn't exist, display an appropriate message 
# instead of allowing the program to crash.
import os
filename=input("enter file name")
if os.path.exists(filename):
    print("File Exists and deleting the file")
    os.remove(filename)
else:
    print("file doesn't exist")
# Create a new file only if it doesn't already exist
#  Ask the user for a filename and create it using "x" mode. 
# If a file with the same name already exists, handle the situation appropriately.
filename=input("enter a file name")
try:
    with open(filename,"x"):
        print("file opened successfully")
except FileExistsError:
    print("file already exists")

    
# Handle invalid number input
#  Ask the user to enter two numbers and calculate their sum. 
# Handle the situation where the user enters text instead of a number using try-except.
try:
    num1,num2=map(int,input("enter 2 numbers").split())
except ValueError:
    print("enter integers only")
else:
    print(num1+num2)
# Handle division errors
#  Ask the user for two numbers and divide the first by the second. Handle:
# Invalid number input
# Division by zero
# Handle file errors
try:
    num1,num2=map(int,input("enter 2 numbers").split())
    print(num1/num2)
except ValueError:
    print("enter integers only")
except ZeroDivisionError:
    print("number can't be zero")
    

#  Ask the user for a filename and attempt to open it in read mode. 
# Handle the situation where:
# The file doesn't exist.
# Another unexpected error occurs.

filename=input("enter the file name")
try:
    f=open(filename,"r")
    content=f.read()
except FileNotFoundError:
    print("file not found")
except Exception:
    print("Unexpected error occured")
else:
    
    print(content)

# File + Exception Handling Challenge
#  Create a program that asks the user for a filename and a number.
