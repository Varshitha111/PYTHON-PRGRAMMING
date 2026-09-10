# 9. Basic Recursion
# Write a recursive function to calculate the factorial of a number. Example: Input 5 → Output 120.
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
# Write a recursive function to find the sum of numbers from 1 to n. Example: Input 5 → Output 15.
def recursive_demo(n):
    if n==1:
        return 1
    else:
        return n+recursive_demo(n-1)
print(recursive_demo(5))