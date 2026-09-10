# 11. Loop Control – 
# break
# Keep taking numbers from the user until the user enters 00
# Print the sum of all numbers entered before 0
# Example:
# Input:
# 10
# 20
# 5
# 0
# Output:
# 35
def sum_num():
    sum=0
    while True:
        n=int(input("enter num"))
        if n==0:
            break
        sum+=n
    return sum
print(sum_num())