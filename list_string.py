# 18. Lists + Strings
# Given:
# words = ["apple", "banana", "kiwi", "orange", "grape"]
# Create a new list containing only words whose length is greater than 
# Expected output:
# 5 .
# 6
# ["banana", "orange"]
words = ["apple", "banana", "kiwi", "orange", "grape"]
l=[]
for i in words:
    if len(i)>5:
        l.append(i)
print(l)