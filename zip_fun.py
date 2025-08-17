# What is the purpose of zip function in python?
# The zip function is used to combine two or more iterables (like lists or tuples) into a single iterable of tuples.
# Each tuple contains elements from the input iterables that are at the same position.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
for item in zipped:
    print(item)
    print(list(item))  # Convert tuple to list for better readability
