# 8. String Methods
# Given the sentence:
# Python is very easy to learn
# Write a program to: 1. Count the number of words. 2. Convert the sentence to uppercase. 3. Replace 
# "easy" with 
# "powerful" 
def string_operations(s):
    count=0
    s1=s.split(" ")
    # for i in s1:
    #     count+=1
    print(len(s1))
    uppercase=s.upper()
    s.replace("easy","powerful")
    print(uppercase)
    print(s)
string_operations("Python is very easy to learn")