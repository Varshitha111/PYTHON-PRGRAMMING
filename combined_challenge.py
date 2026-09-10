# 20. Combined Challenge
# Given:
# numbers = [10, 25, 30, 45, 50, 75, 90, 100]
# Create a new list containing numbers that:
# Are greater than
# Are divisible by
# 30
# 5
# Do not include
# Expected output:
# 75
# [45, 50, 90, 100]
numbers = [10, 25, 30, 45, 50, 75, 90, 100]
new_list=[]
for i in numbers:
    if i>30 and i%5==0 and i!=75:
        new_list.append(i)
print(new_list)