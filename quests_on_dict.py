# 7. Dictionaries
# Given students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}, 
# find the student with the highest marks.
students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
maxi=0
topper=""
for key,value in students.items():
    if value>maxi:
        maxi=value
        topper=key
print(topper)
# Given a dictionary containing student names and marks, calculate the average marks.
students = {"Rahul": 85, "Priya": 92, "Amit": 78, "Sneha": 95, "Karan": 88}
avg=0
count=0
for key,value in students.items():
    avg+=value
    count+=1
avg=avg/count
print(avg)
# Take a sentence as input and create a dictionary containing the frequency of each word.
# Example: "apple banana apple mango banana apple" → {"apple": 3, "banana": 2, "mango": 1}.
sentence="apple banana apple mango banana apple"
sentence=sentence.split(" ")
dictionary={}
for i in sentence:
    dictionary[i]=dictionary.get(i,0)+1
print(dictionary)
# Given two dictionaries, combine them into a single dictionary.
students = {"Rahul": 85, "Priya": 92}
students1={"Amit": 78, "Sneha": 95, "Karan": 88}
print(students|students1)

