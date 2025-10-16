# Closures in Python

``Closure`` is a technique which allows the storing of values in spite of the fact that
the context in which they have been created does not exist anymore.

A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

## Example of a Closure

```python
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


hi_func = outer_function('Hi')
bye_func = outer_function('Bye')
hi_func()  # Output: Hi
bye_func()  # Output: Bye
```