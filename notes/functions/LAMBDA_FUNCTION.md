# Lambda Function in Python

A ``lambda`` function is a small anonymous function defined using the `lambda` keyword in Python. It can take any number
of arguments but can only have one expression. The expression is evaluated and returned when the function is called.

````txt
A `lambda` function is a function without a name (an anonymous function).
````

## Syntax

```txt
lambda arguments: expression
```

- `lambda` is the keyword used to define a lambda function.
- `arguments` are the input parameters (can be zero or more).
- `expression` is a single expression that is evaluated and returned.
- The ``type`` of a lambda function is `<class 'function'>`.

## Example

````python
# anonymous parameterless function
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# anonymous function with one parameter
square = lambda x: x * x
print(square(5))  # Output: 25
````

## map() function with lambda

The `map()` function applies a given function to all items in an iterable (like a list) and returns a map object (an
iterator).

````txt
The ``map()`` function applies the function passed by its first argument to all its second argument's elements, and
returns an iterator delivering all subsequent function results.
````

````python
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, numbers)

print(type(squared))  # Output: <class 'map'>
print(squared)  # Output: <map object at 0x...>
print(squared.__next__())  # Output: 1
print(next(squared))  # Output: 4
print(list(squared))  # Output: [9, 16, 25]
````

## filter() function with lambda

The `filter()` function constructs an iterator from elements of an iterable for which a function returns true.

### Syntax

````txt
filter(function, iterable)
````

- `function` is a function that tests if each element of the iterable is true or false.
- `iterable` is an iterable like sets, lists, tuples, etc.

````python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(type(even_numbers))  # Output: <class 'filter'>
print(list(even_numbers))  # Output: [2, 4, 6]
````

## reduce() function with lambda

## Summary

- A ``lambda function`` is a tool for creating anonymous functions
- The ``map(fun, list)`` function creates a ``copy`` of a ``list`` argument, and applies the ``fun`` function to all of
  its elements, returning a ``generator`` that provides the new list content element by element.

````python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
````

- The ``filter(fun, list)`` function creates a`` copy ``of those ``list`` elements, which cause the ``fun ``function to
  return ``True``. The function's result is a ``generator`` providing the new list content element by element.








