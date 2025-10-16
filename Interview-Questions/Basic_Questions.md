## Question 1 – Data Types & Mutability

In Python, which built-in data types are mutable and which are immutable?
Also, why does immutability matter when using objects as dictionary keys?

* Immutable built-ins: ``int``, ``float``, ``bool``, ``str``, ``tuple``, ``frozenset``, ``bytes``.
* Mutable built-ins:`` list``,`` dict``, ``set``, ``bytearray``.

```txt
Python uses a hash table for dicts. Keys must be ``hashable`` → their hash must stay constant for their lifetime, which is guaranteed only for immutable objects.
````
---

## Question 2 – Lists vs Tuples

How are lists and tuples stored internally in Python, and why is a tuple generally faster than a list when iterating?

* Lists in CPython

  - Implemented as a dynamic array of pointers to PyObject.
  - They over-allocate space to support fast appends (amortized O(1)).
  - Elements can be added/removed, so extra bookkeeping is needed.

* Tuples

    - Also store pointers to PyObject, but the size is fixed at creation.
    - No over-allocation or resizing logic, so less memory & simpler iteration.

````
➡️ Because tuples don’t need to check for potential resizes or manage free slots, iterating over them is a bit faster than over lists.
````
---- 

## Question 3 – Variable Binding & is vs ==

What is the difference between the is operator and the == operator in Python?
Give an example where ``a is b`` is ``False`` but `` a == b`` is ``True``.

* ``is`` checks `object identity` (whether two variables point to the ``same object`` in memory).
* `==` checks value equality (whether `__eq__` is defined to return for those objects).

Example where a is b is False but a == b is True:
```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (values are equal)
print(a is b)  # False (different list objects in memory)

```

```python
# Python automatically “interns” some strings for efficiency.
# Simple string literals (letters, digits, _, no spaces or special chars) often share the same memory object.

aStr = "something"
otherStr = "something"

print(aStr is otherStr) # True
print(aStr == otherStr) # True

```

## Question 5 – Functions & Defaults

```python
def append_item(item, lst=[]):
    lst.append(item)
    return lst
```
What happens if you call append_item(1) multiple times? Why does it behave that way, and how would you fix it?

```
the default value is evaluated only once, at function definition time.

lst=[] is created a single time, and every call without a lst reuses the same list
```

```python
print(append_item(1))  # [1]
print(append_item(2))  # [1, 2]  <-- keeps growing!
```

✅ Fix: Use `` None`` as the default and create a new list inside:
```python
def append_item(item,lst=None):
    if lst is None:
        lst=[]
    lst.append(item)
    return lst    
```
