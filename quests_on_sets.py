# 6. Sets
# Given two sets, find their union, intersection, and difference.
set1={1,2,3,4,5,6}
set2={9,7,6,4,2,1,4}
print(set1.union(set2))
print(set2.intersection(set2))
print(set1.difference(set2))
# Given a list of numbers, use a set to find all the duplicate elements.
list1=[1,2,3,4,5,6,4,1,2,3]
print(list(set(list1)))
# Given two sets of student names, find the students who are present in both sets.
students1={"varshitha","sudha","sushma"}
students2={"varshitha","pranathi","harini"}
print(students1.intersection(students2))
