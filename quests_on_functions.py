# 8. Functions
# Write a function is_prime(n) that returns True if a number is prime and False otherwise.
def is_prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        
print(is_prime(9))
# Write a function find_largest(numbers) that takes a list of numbers 
# and returns the largest number without using max().
def find_largest(numbers):
    largest=numbers[0]
    for i in numbers:
        if i>largest:
            largest=i 
    print(largest)
find_largest([1,92,3,2,4,42])