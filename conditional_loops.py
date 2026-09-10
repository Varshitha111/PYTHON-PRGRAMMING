# 3. Conditional Statements & Loops
# Print all numbers from 1 to 100 that are divisible by both 3 and 5.
for i in range(1,100):
    if i%3==0 and i%5==0:
        print(i)
# Take a number n and print its multiplication table from 1 to 10.
def multi_table(n):
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")
multi_table(5)
# Take a number and find the sum of its digits.
def sum_of_digits(n):
    # last_digit=0
    # rem=0
    i=n
    sum=0
    while i>0:
        sum+=i%10
        i=i//10
    print(sum)
sum_of_digits(32)
# Take a number and check whether it is a prime number.
def check_prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("prime number")
    else:
        print("not prime")
check_prime(9)
# Print the following pattern for n = 5: *, **, ***, ****, ***** (one row per line).
def pattern(n):
    for i in range(1,n+1):
        print("*"*i)
pattern(5)
