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
