# max() -> Returns the largest item in an iterable or the largest of two or more arguments.
# min() -> Returns the smallest item in an iterable or the smallest of two or more arguments.
# sum() -> Sums the items of an iterable from left to right and returns the total.
# abs() -> Returns the absolute value of a number.
# round() -> Rounds a floating-point number to the nearest integer or to a specified number of decimal places.
# len() -> Returns the number of items in an object.
# type() -> Returns the type of an object.
# id() -> Returns the unique identifier of an object.
# isinstance() -> Checks if an object is an instance of a specified class or a tuple of classes.

nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]

print("Max:", max(nums))          # Output: 9
print("Min:", min(nums))          # Output: 1
print("Sum:", sum(nums))          # Output: 36
print("Len(nums):", len(nums))    # Output: 9
print("Type(nums):", type(nums))  # Output: <class 'list'>
print("ID(nums):", id(nums))      # Output: Unique identifier (varies)
print("Isinstance(nums, list):", isinstance(nums, list))  # Output: True

