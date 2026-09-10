# 15. Lists + Conditions
# Given a list of numbers, count how many numbers occur more than once.
# Example:
# Input:
# [1, 2, 3, 2, 4, 1, 5]
# Output:
# 2
# Here, 
# 1 and 
# 2 are repeated.
def list_condition(l):
    count=0
    l1=[]
    for i in l:
        if i in l1:
            count+=1
        else:
            l1.append(i)
    print(count)
list_condition([1, 2, 3, 2, 4, 1, 5])      