# List Summary

1) The ``list is a type of data`` in Python used to ``store multiple objects``.
   It is an ``ordered and mutable collection`` of comma-separated items between square brackets, e.g.:

```python
my_list = [1, None, True, "I am a string", 256, 0]
````

2) Lists are ``indexed``,``updated`` and ``sliced`` using ``zero-based indexing``.
   You can access elements using their index, e.g.:

```python
my_list = [1, None, True, "I am a string", 256, 0]
first_element = my_list[0]  # Accessing the first element
last_element = my_list[-1]  # Accessing the last element
sliced_list = my_list[1:4]  # Slicing from index 1 to index 3 (inclusive of start, exclusive of end)

my_list[1] = "Updated"  # Updating the second element
my_list.insert(2, "Inserted")  # Inserting at index 2 
my_list.append("Appended")  # Appending at the end of the list
```

3) Lists can be nested, e.g.:

```python
my_list = [1, 'a', ["list", 64, [0, 1], False]]
nested_element = my_list[2][2][1]  # Accessing the element '1' from the nested list
```

4) List elements and lists can be deleted, e.g.:

```python
my_list = [1, 'a', ["list", 64, [0, 1], False]]

my_list.pop()  # Removing the last element
my_list.pop(1)  # Removing the second element

my_list.remove('a')  # Removing the first occurrence of 'a'

del my_list[1]  # Deleting the second element
del my_list[1][2]  # Deleting the nested list [0, 1]
del my_list  # Deleting the entire list
```

5) Lists can be iterated through using the for loop, e.g.:

```python
my_list = [1, 'a', ["list", 64, [0, 1], False]]
for item in my_list:
    print(item)
```

6) List slicing supports various operations, such as: ```[start:end:step]```
    - `start`: The starting index of the slice (inclusive).
    - `end`: The ending index of the slice (exclusive).
    - `step`: by default is 1.
    - `my_list[start:end]`: Returns a new list containing elements from index `start` to `end-1`.
    - `my_list[start:end:step]`: Returns a new list containing elements from index `start` to `end-1`, taking every `step`-th element.
    - Omitting `start` defaults to the beginning of the list, and omitting `end` defaults to the end of the list.
    - Negative indices can be used to slice from the end of the list.

```python
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[2:7])  # Output: [2, 3, 4, 5, 6]
print(my_list[:5])  # Output: [0, 1, 2, 3, 4]
print(my_list[5:])  # Output: [5, 6, 7, 8, 9]
print(my_list[::2])  # Output: [0, 2, 4, 6, 8]
print(my_list[1:8:3])  # Output: [1, 4, 7]
print(my_list[-5:-1])  # Output: [5, 6, 7, 8]
print(my_list[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

7) ``in`` operator can be used to check for membership in a list, e.g.:

```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False
print(5 not in my_list)  # Output: False
```

8) Lists support various methods for manipulation, such as:
    - `append()`: Adds an item to the end of the list.
    - `extend()`: Extends the list by appending elements from another iterable.
    - `insert()`: Inserts an item at a given position.
    - `remove()`: Removes the first occurrence of a value.
    - `pop()`: Removes and returns an item at a given index (default is the last item).
    - `clear()`: Removes all items from the list.
    - `index()`: Returns the index of the first occurrence of a value.
    - `count()`: Returns the number of occurrences of a value.
    - `sort()`: Sorts the list in ascending order (can take a custom key function).
    - `reverse()`: Reverses the elements of the list in place.
    - `copy()`: Returns a shallow copy of the list.