# 13. Lists
# Given:
# numbers = [12, 5, 8, 21, 4, 15, 10]
# Find:
# Largest number
# Smallest number
# Sum of all numbers
# Do not use 
# max() , 
# min() , or 
# sum() .
def list_operations(l):
    max_num=l[0]
    min_num=l[0]
    sum=0
    for i in l:
        if i>max_num:
            max_num=i
        if i<min_num:
            min_num=i
        sum+=i
    print("largest num:",max_num)
    print("smallest number",min_num)
    print("sum of all numbers",sum)
list_operations([12, 5, 8, 21, 4, 15, 10])