# Difference between 'is' and '==' operators
# 'is' checks for object identity
# '==' checks for value equality
list1 = [1,2,3]
list2 = [1,2,3]
list1 = list2
print(list1 is list2) # True, because list1 and list2 refer to the same object
print(list1 == list2) # True, because the values are the same

# What is the purpose of the 'enumerate' function?
# The 'enumerate' function adds a counter to an iterable and returns it as an enumerate object.
# This is useful when you need a counter with the values from the iterable.

my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")