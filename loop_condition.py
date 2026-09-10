# 7. Loops + Conditions
# Given a number N, count how many digits in the number are even.
# Example:
# Input: 583246
# Output: 3
def loop_condition(n):
    last_digit=0
    temp=n
    count=0
    while temp>0:
        last_digit=temp%10
        if last_digit%2==0:
            count+=1
        temp=temp//10
    print(count)
loop_condition(583246)