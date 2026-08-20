# 17. Nested Lists
# Given:
# numbers = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]
# ]
# Calculate the sum of all elements.
# Expected output:
# 45
numbers = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
sum=0
for i in numbers:
    for j in i:
        sum+=j
print(sum)