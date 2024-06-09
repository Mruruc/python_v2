"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered:
    When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
    added items will be placed at the end of the list.

Changeable:
    The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

"""

# Create a List:
# Lists are created using square brackets:

nums = [1, 2, 3, 4, 5]

# List Length:
# To determine how many items a list has, use the len() function:
print(len(nums))
print(type(nums))

# List can contain different data types:
# A list with strings, integers and boolean values:
list1 = ["apple", "banana", "cherry", 1, 2, 3, True, False]
print(list1)

for index in range(len(list1) - 1):
    print(index, '=>', list1[index])
