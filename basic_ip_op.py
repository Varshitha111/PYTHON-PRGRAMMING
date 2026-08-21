# 1. Basics & Input/Output
# Take two integers as input and print their sum, difference, product, and division.
num1,num2=map(int,input("enter num1 and num2").split())
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
# Take a user's name and age as input and print: Hello Rahul, you are 21 years old.
name=input("enter name")
age=int(input("enter age"))
print(f"Hello {name}, you are {age} years old.")
# Take a number as input and check whether it is positive, negative, or zero.
num=int(input("enter num"))
if num>0: print("positive") 
elif num<0: print("negative") 
else: print("zero")
# Take three numbers as input and print the largest number.
number1,number2,number3=map(int,input("enter 3 nums").split())
if number1>number2 and number1>number3:
    print(number1)
elif number2>number3 and number2>number1:
    print(number2)
else:
    print(number3)