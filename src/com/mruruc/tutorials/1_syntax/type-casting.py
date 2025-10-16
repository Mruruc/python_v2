"""
Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting.
Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals),
 or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal,
a float literal or a string literal (providing the string represents a float or an integer)

4_str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

"""

intType = int(123)
floatType = float("54")
strType = str(45.00)

print(type(intType), intType)
print(type(floatType), floatType)
print(type(strType), strType)
