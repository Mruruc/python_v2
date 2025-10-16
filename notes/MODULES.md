# Python Modules

- A module is a file containing Python definitions and statements.
- The file name is the module name with the suffix `.py` appended.
- Modules can define functions, classes, and variables that can be reused in other Python programs.
- Within a module, the module's name is available as the value of the global variable `__name__`.

## Creating a Module

To create a module, simply save the code you want in a file with a `.py`
extension.

## Module aliasing

You can give a module an alias when you import it, which can be useful to
shorten long module names or avoid name conflicts.

```python
import module_name as alias
```

## dir() function

The function returns an alphabetically sorted list containing all entities' names available in the module identified by
a name passed to the function as an argument
```python
import module_name
print(dir(module_name))
```