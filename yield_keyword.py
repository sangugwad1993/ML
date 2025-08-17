# What is the purpose of 'yield' keyword in python?
# The 'yield' keyword is used in a function to make it a generator.
# A generator is a special type of iterator that generates values on the fly and can be paused and resumed.
# This is useful for working with large datasets or streams of data where you don't want to load everything into memory at once.

def my_generator(n):
    for i in range(n):
        yield i**2

gen = my_generator(10)
for value in gen:
    print(value)
