# Create a set of 5 numbers and add a new number using add().
s={1,2,3,4,5}
s.add(6)
print(s)
# Given {10, 20, 30, 40}, remove 30 from the set.
set2={10, 20, 30, 40}
set2.remove(30)
print(set2)
# Given {1, 2, 3} and {3, 4, 5}, find their union.
set3={1, 2, 3} 
set4={3, 4, 5}
print(set3|set4)
# Given {1, 2, 3, 4} and {3, 4, 5, 6}, find their intersection.
set5={1, 2, 3, 4} 
set6={3, 4, 5, 6}
print(set5&set6)
# Given {1, 2, 3, 4} and {3, 4, 5}, find the elements present only in the first set.
set7={1, 2, 3, 4} 
set8={3, 4, 5}
print(set7-set8)
# Given {1, 2, 3} and {2, 3, 4}, find the symmetric difference.
set9={1,2,3}
set10={2,3,4}
print(set9 ^ set10)
# Create a set containing duplicate values and remove all duplicates.
set11={1,2,3,41,1}
print(set11)
# Given two sets, check whether they have any common elements.
set12={1,2,3,4,5}
set13={3,4,5,6}
print(set12&set13)
# Create a set and remove all its elements using clear().
set14={1,2,3,4,5,6,7}
set14.clear()
print(set14)
# Given {10, 20, 30, 40}, check whether 20 exists in the set.
set15={10, 20, 30, 40}
if 20 in set15:
    print("20 exists")
else:
    print("doesn't exist")