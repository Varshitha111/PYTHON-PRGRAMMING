# Create a file hello.txt containing "Hello Python". Read the entire file using read() and print it.
file=open("hello.txt","r").read()
print(file)

# Create a file containing a student's name, age, and course. 
# Read the complete file using read() and display it.
read_student_data=open("studentdetails.txt","r").readlines()
print(read_student_data)

# Create a file containing 5 names. Use readlines() to read all names and print them one by one.
read_names=open("names.txt","r").readlines()
print(read_names)

# Create a file containing 5 numbers, one per line. Use readlines() to calculate their sum.
calculate_sum=open("numbers.txt","r").readlines()
sum=0
for num in calculate_sum:
    sum+=int(num)
print(sum)
# Create a file containing three lines. Use readline() to read and print each line separately.
read_lines=open("readinglines.txt","r").readlines()
for line in read_lines:
    print(line)
    
# A file contains a student's name, age, and marks on separate lines. 
# Use readline() to read all three values and display them.
read_lines=open("students_agemarks.txt","r").readlines()
print(read_lines)
# Read a file line by line using a for loop and print every line.
read_lines=open("students_agemarks.txt","r").readlines()
for line in read_lines:
    print(line)
# Read a file containing numbers and use a for loop to print only the even numbers.
calculate_sum=open("numbers.txt","r").readlines()
for num in calculate_sum:
    if int(num)%2==0:
        print(num)

# Read a file containing names and print only names whose length is greater than 5.
read_names=open("names.txt","r").readlines()
for name in read_names:
    if len(name)>5:
        print(name)
# Read a file containing numbers and find the largest and smallest number using a for loop.
calculate_sum=open("numbers.txt","r").readlines()
largest=int(calculate_sum[0])
smallest=int(calculate_sum[0])
for num in calculate_sum:
    if int(num)>largest:
        largest=int(num)
    if int(num)<smallest:
        smallest=int(num)
print(f"largest number is {largest},smallest number is {smallest}")

# Create a file students.txt and write 5 student names into it using write().
students_file=open("students.txt","w")
students_file.write("varshitha harini marina jessica pranay")
students_file.close()
students_files=open("students.txt","r").readline()
print(students_files)
# Create a file and write numbers from 1 to 10, with each number on a separate line.
calculate_sum=open("numbers.txt","r").readlines()
for num in calculate_sum:
    print(num)
# Take 5 names from the user using input() and write them into a file.
with open("input_names","w") as file:
    for name in range(5):
        name=input("enter a name")
        file.write(name+"\n")
with open("input_names","r") as file:
    content=file.read()
print(content)
# Take 5 numbers from the user and write them into a file, one number per line.
with open("input_numbers","w") as file:
    for i in range(5):
        i=input("enter num")
        file.write(i+"\n")
        
with open("input_numbers","r") as file:
    content=file.readlines()
for num in content:
    print(num)
# Create a file containing:
# Rahul 80
# Aman 35
# Priya 92
# Neha 45
# Read the file and print only students who scored 50 or above.
with open("marks_of_students.txt","r") as file:
    for line in file:
        name,marks=line.split()
        if int(marks)>=50:
            print(name)
            
# Create a file containing a paragraph. Use read() to count the total number of words.
with open("para.txt","r") as file :
    content=file.read()
words=content.split()
print(f" number of words{len(words)}")
# Create a file containing 10 numbers. Use readlines() to calculate their average.
with open("numbers.txt","r") as file:
    content=file.readlines()
sum=0
count=0
for num in content:
    sum+=int(num)
    count+=1
avg=sum/count
print(avg)
# Create a file containing several names. 
# Read the file using a for loop and count how many names are present.
with open("names.txt","r") as file:
    content=file.readlines()
count=0
# content=content.split()
for i in content:
    count+=1
print(count)
# Create a simple student record program that asks for name, age, and marks, 
# writes them to student.txt, and then reads the file and displays the information.
name=input("enter name")
age=int(input("enter age"))
marks=int(input("enter marks"))
with open("student.txt","a") as file:
    file.write(str(name))
    file.write(str(age))
    file.write(str(marks))

with open("student.txt","r") as file:
    content=file.read()
print(content)
# Create a program that:
# Takes 5 student names from the user.
# Writes them to a file.
# Reads the file using a for loop.
# Prints each student with a serial number.
with open("loop_student.txt","a") as file:
    for i in range(1,6):
        name=input("enter a name")
        file.write(f"{i}\t")
        file.write(f"{name}\n")
with open("loop_student.txt","r") as file:
    content=file.read()
print(content)