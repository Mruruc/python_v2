# Reflection and Introspection

## Introspection

The ability of a program to examine the type or properties of an object at runtime.

## Reflection

The ability of a program to manipulate the values, properties and/or functions of an object at th runtime.

````txt
In the other words, you do not have to know a complete class/object definiton to manipulate the object, 
as the object and/or its class contain the metadata allowing you to recognize its features during the program execution.
````

----
## Example

````python
````

---

## Notes

```txt
A method is a function embedded inside a class. The first (or only) parameter of each method is usually named self, 
which is designed to identify the object for which the method is invoked in order to access the object's properties or invoke its methods.
```

---

````txt
 If a class contains a constructor (a method named __init__) it cannot return any value and cannot be invoked directly.
````

---

````txt
All classes (but not objects) contain a property named __name__, which stores the name of the class. 
Additionally, a property named __module__ stores the name of the module in which the class has been declared, 
while the property named __bases__ is a tuple containing a class's superclasses.
````