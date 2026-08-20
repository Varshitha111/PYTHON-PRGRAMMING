# 0. String Methods + Loops
# Given a string, count how many characters are:
# Vowels
# Consonants
# Digits
# Example:
# 3
# Input:
# hello123
# Output:
# Vowels: 2
# Consonants: 3
# Digits: 3
def str_loop(s):
    countvow,countdigit,countcons=0,0,0
    vow="aeiouAEIOU"
    digit="1234567890"
    for i in range(0,len(s)):
        if s[i] in vow:
            countvow+=1
        elif s[i] in digit:
            countdigit+=1
        else:
            countcons+=1
    print(f"vowels:{countvow}")
    print(f"Consonants:{countcons}")
    print(f"Digits:{countdigit}")
str_loop("hello123")