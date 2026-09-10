# 5. Tuples
# Given a tuple of numbers, find the sum, maximum, and minimum values.
tuple1=(1,2,3,4,5,6,7,8)
# sum=0
# for i in tuple1:
#     sum+=i
#     maximum,minimum=tuple1[0],tuple1[0]
#     if i>maximum:
#         maximum=i
#     if i<minimum:
#         minimum=i
# print(maximum,minimum,sum)
print(sum(tuple1))
print(max(tuple1))
print(min(tuple1))

# Given the tuple (10, 20, 10, 30, 10, 40, 20), find how many times 10 and 20 occur.
tuple2= (10, 20, 10, 30, 10, 40, 20)
print(tuple2.count(10))
print(tuple2.count(20))