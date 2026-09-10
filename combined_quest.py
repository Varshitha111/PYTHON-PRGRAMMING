# 19. Combined Question
# Given the sentence:
# Python is easy and Python is powerful
# Convert it into a list of words and find how many times 
# Expected output:
# 2
# "Python" occurs.
# Do not use 
# count() .
s="Python is easy and Python is powerful"
s=s.split(" ")
count=0
for i in s:
    if i=="Python":
        count+=1
print(count)