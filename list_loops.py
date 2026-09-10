# 4. Lists + Loops
# Given a list of integers, create a new list containing only numbers greater than 10
# Example:
# Input:
# [4, 15, 8, 21, 3, 17]
# Output:
# [15, 21, 17]
def list_loops(l):
    l1=[]
    for i in l:
        if i>10:
            l1.append(i)
    print(l1)
list_loops( [4, 15, 8, 21, 3, 17])