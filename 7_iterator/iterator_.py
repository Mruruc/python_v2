"""
An iterator is an object that contains countable number of values.
Technically, in Python, an iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__().
"""

fruits = ("apple", "banana", "cherry")

iterator = iter(fruits)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# print(next(iterator))

print(type(iterator))

print("==============================")

for fruit in fruits:
    print(fruit)

# The for loop actually creates an iterator object and executes the next() method for each loop.
