# Nuance Cases in Python

## 1) Swapping Variables

````python
var = 10
var2 = 20

# Swapping using a temporary variable
temp = var
var = var2
var2 = temp
print(f"var: {var}, var2: {var2}")

# Swapping without a temporary variable
#  20,  10
var, var2 = var2, var
print(f"var: {var}, var2: {var2}")

# How is it working?
# ✅ So:
# Tuple packing (right side) + tuple unpacking (left side)
# var, var2 = (var2, var)
# var, var2 = (20, 10)
# var = 20
# var2 = 10
````

2) ## Functions and Methods

A ``function`` is defined using the `def` keyword and can take parameters and return values.
A ``method`` is a function that is associated with an object and is called on that object.

````python
# Function
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))  # Output: Hello, Alice!
# Method
my_list = [1, 2, 3]
my_list.append(4)  # append() is a method of the list object
print(my_list)  # Output: [1, 2, 3, 4
````