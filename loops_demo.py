# 5. Loops
# Given an integer N, print all numbers from 1 to N that are divisible by both 3 and 5.
# Example:
# Input: 30
# Output: 15 30
def loop_demo(n):
    for i in range(1,n+1):
        if i%5==0 and i%3==0: print(i)
loop_demo(200)