# 9. String Comparison
# Given a sentence containing space-separated words, print the lexicographically smallest word.
# Example:
# Input:
# banana apple mango cherry
# Output:
# apple
# Do not use 
# min() 
def str_compare(s):
    s=s.split(" ")
    lowest=s[0]
    for i in s:
        if i<lowest:
            lowest=i
    print(lowest)
str_compare("banana apple mango cherry")