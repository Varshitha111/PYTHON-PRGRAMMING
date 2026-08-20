# 6. Loops + Arithmetic
# Given N, calculate the sum of all even numbers from 1 to N.
# Example:
# Input: 10
# Output: 30
def loop_arithmetic(n):
    sum=0
    for i in range(1,n+1):
        if i%2==0: sum+=i
    print(sum)
loop_arithmetic(10)