# 4. Lists
# Given a list of numbers, find the largest and smallest element without using max() or min().
def max_min(lst):
    maximum=lst[0]
    minimum=lst[0]
    for i in lst:
        if i>maximum:
            maximum=i
        if i<minimum:
            minimum=i 
    print(f"maximum is {maximum} and minimum is {minimum}")
max_min([1,2,9,3,4,32])
# Given a list, create a new list containing only the even numbers.
def even_list(l):
    new_list=[]
    for i in l:
        if i%2==0:
            new_list.append(i)
    print(new_list)
even_list([1,2,9,3,4,32])
# Given [10, 20, 10, 30, 20, 40, 30], remove the duplicates and create a list containing only unique values.
def no_dup(lst):
    new_list=set(lst)
    new_list=list(new_list)
    print(new_list)
no_dup([10, 20, 10, 30, 20, 40, 30])
list1=[10, 20, 10, 30, 20, 40, 30]
l2=[]
for i in list1:
    if i not in l2:
        l2.append(i)
print(l2)
# Given a list of numbers, find the second-largest element.
list1=[10, 20, 10, 30, 20, 40, 30]
largest=list1[0]
second_largest=list1[0]
for i in list1:
    if i>largest:
        second_largest=largest
        largest=i
    elif i<largest and i>second_largest:
        second_largest=i
print(second_largest)