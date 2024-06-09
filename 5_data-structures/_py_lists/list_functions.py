# List Functions:
nums = [9, 5, 20, 6]

# The insert() method inserts an element to the list at a given index.

# nums.insert(5,6)
# nums.insert(1, 60)

# append() method adds item to the end of the list.
# nums.append(106)

# extend() method appends element/s from another iterable(list,tuples,set,dictionaries) to the current list
nums.extend([9, 8, 47])

# remove() method removes the specified item from the list with first occurrence.
# pop() method removes item in list with specified index,
# if index is not specified will remove the last element in list.

# print("Before Removing:", nums)
# nums.remove(47)
# nums.pop()
# nums.pop(0)
# print("After removing :", nums)

# clear() method empties the list.
nums.clear()
print(dir(nums))






