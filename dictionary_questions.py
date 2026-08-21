# Create a dictionary containing a student's name, age, and marks and print each value.
dict1={"name":"varshitha","age":21,"marks":89}
print(dict1)
# Given {"name": "Rahul", "age": 20}, add a new key city.
dict2={"name": "Rahul", "age": 20}
dict2["city"]="hyd"
print(dict2)
# Given {"name": "Rahul", "age": 20}, update the age to 21.
dict3={"name": "Rahul", "age": 20}
dict3["age"]=21
print(dict3)
# Given {"name": "Rahul", "age": 20, "city": "Hyderabad"}, remove the city key.
dict4={"name": "Rahul", "age": 20, "city": "Hyderabad"}
del dict4["city"]
print(dict4)
# Given a dictionary, check whether a particular key exists.
dict5={"name": "Rahul", "age": 20, "city": "Hyderabad"}
if "city" in dict5:
    print("key exists")
else:
    print("key doesn't exist")
# Given {"apple": 50, "banana": 30, "mango": 40}, print all the keys.
dict6={"apple": 50, "banana": 30, "mango": 40}
for key in dict6:
    print(key)
# Given {"apple": 50, "banana": 30, "mango": 40}, print all the values.
dict7= {"apple": 50, "banana": 30, "mango": 40}
for value in dict7.values():
    print(value)
# Given a dictionary, use items() to print every key and value.
dict8= {"apple": 50, "banana": 30, "mango": 40}
for key,value in dict8.items():
    print(key,value)
# Given {"a": 10, "b": 20, "c": 30}, find the sum of all values.
dict9={"a": 10, "b": 20, "c": 30}
sum=0
for value in dict9.values():
    sum+=value
print(sum)
# Given a dictionary containing student names and marks, find the student who has the highest marks.
students={"varsh":90,"harini":98,"sneha":99}
highest=0
student=""
for key,value in students.items():
    if value>highest:
        highest=value
        student=key
print(student,highest)
    
    