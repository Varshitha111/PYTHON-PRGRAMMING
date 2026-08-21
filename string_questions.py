# 2. Strings
# Take a string as input and count the number of vowels in it.
vow="AEIOUaeiou"
str1="apple"
# str1=input("enter string")
count=0
for i in str1:
    if i in vow:
        count+=1
print(count)
# Take a string and print it in reverse without using a built-in reverse function.
string1="banana"
print(string1[::-1])
rev=""
for i in string1:
    rev=i+rev
print(rev)
# Take a string and check whether it is a palindrome.
string2="mom"
str_dup=string2[::-1]
if str_dup==string2:
    print("palindrome")
else:
    print("not a palindrome")
# Take a sentence and find the longest word in it.
sentence="varshithareddy I am varshitha"
longest=""
# current=sentence[0]
sentence=sentence.split(" ")
for i in sentence:
    if i>longest:
        longest=i 
print(longest)