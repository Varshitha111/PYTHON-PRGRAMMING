l1=[1,2,3,4,5]
l1.append(6)
print(l1)
l_of_names=["varshitha","chitti","ammulu"]
l_of_names.insert(2,"rahul")
print(l_of_names)
# Given [10, 20, 30, 20, 40, 20], remove the first occurrence of 20.
l2=[10, 20, 30, 20, 40, 20]
l2.remove(20)
print(l2)
# Given [5, 2, 8, 1, 9], sort the list in ascending and descending order.
l3=[5, 2, 8, 1, 9]
print(sorted(l3))
rev=sorted((l3),reverse=True)
print(rev)

# Given [10, 20, 30, 40, 50], remove the last element and print the removed element.
l4=[10, 20, 30, 40, 50]
print(l4.pop())
print(l4)
# Given [1, 2, 2, 3, 2, 4], find how many times 2 occurs.
l5=[1, 2, 2, 3, 2, 4]
print(l5.count(2))
# Given ["apple", "banana", "mango", "orange"], find the index of "mango".
fruits=["apple", "banana", "mango", "orange"]
print(fruits.index("mango"))
# Create two lists and combine the second list into the first using extend().
list_1=[1,2,3,4,5]
list_2=[6,7,8,9]
list_1.extend(list_2)
print(list_1)
# Create a tuple (10, 20, 10, 30, 10, 40) and find how many times 10 occurs.
tuple_1=(10, 20, 10, 30, 10, 40)
print(tuple_1.count(10))
# Given the tuple ("Python", "Java", "C++", "JavaScript"), find the index of "C++".
tuple_2=("Python", "Java", "C++", "JavaScript")
print(tuple_2.index("C++"))
