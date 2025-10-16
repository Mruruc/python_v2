# Generator vs Iterator in Python

## Generator

A Python generator is a special type of function that uses the `yield` keyword to produce a sequence of values lazily (
one at a time, on-demand). When called, a generator function returns a generator object that implements the iterator
protocol. Generators automatically handle the iteration state and provide memory-efficient iteration by generating
values only when requested, rather than storing all values in memory at once.

## Iterator

An iterator is an object that implements the iterator protocol in Python, which consists of two methods:

- `__iter__()`: Returns the iterator object itself
- `__next__()`: Returns the next item in the sequence, or raises `StopIteration` when no more items are available

Iterators maintain their own internal state to track the current position in the sequence and can be traversed only
once (they are consumed as you iterate through them).

## Key Differences

- **Nature**: A generator is a special type of function that creates iterator objects, while an iterator is any object
  that follows the iterator protocol
- **Creation**: Generators are created using `yield` statements in functions or generator expressions, while iterators
  can be custom classes implementing `__iter__()` and `__next__()`
- **Memory efficiency**: Generators are inherently memory-efficient due to lazy evaluation, while custom iterators may
  or may not be depending on implementation
- **Relationship**: All generators are iterators, but not all iterators are generators

---

### Yield Statement

The `yield` statement turns the function into a generator.

When the function is called, it returns a generator object without executing the function body. Each time `next()` is
called on the generator object, the function runs until it hits a `yield` statement, at which point it yields the value
and pauses its state.
The next time `next()` is called, the function resumes execution right after the last `yield` statement.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1


counter = count_up_to(5)
print(type(counter))  # Output: <class 'generator'>, it isn't a function anymore; it's a generator object.
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
```

### List comprehensions vs. generators

List comprehensions create lists in memory, while generator expressions create generators that yield items one at a
time.

````python
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

print(type(the_list))  # Output: <class 'list'>
print(type(the_generator))  # Output: <class 'generator'>
````

### Summary

1) An ``iterator`` is an object of a class providing at least two methods (not counting the constructor):
    * ``__iter__()`` is invoked once when the iterator is created and returns the iterator's object itself;
    * ``__next__() ``is invoked to provide the next iteration's value and raises the ``StopIteration`` exception when
      the
      iteration comes to an end.

2) The ``yield`` statement can be used only inside functions.
    * The ``yield`` statement suspends function execution and causes the
      function to return the yield's argument as a result.
    * Such a function cannot be invoked in a regular way – its only
      purpose is to be used as a generator (i.e. in a context that requires a series of values, like a for loop).


3) A ``**list comprehension**`` becomes a ``generator`` when used inside ``**parentheses**`` (used inside brackets, it
   produces a regular list). For example:










