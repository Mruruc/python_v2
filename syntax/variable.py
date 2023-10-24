x = 5
y = 'john'


print(y)
print(x)

# variables do not need to be declared with any particular type,
# and can even change type after they have been set.


# Casting:

stringType = str(3)  # x will be '3'
integerType = int(3)  # y will be 3
floatType = float(3)  # z will be 3.0

print(stringType)
print(integerType)
print(floatType)

# type() function

print(type(stringType))
print(type(integerType))
print(type(floatType))

# Not: String variables can be declared either by using single or double quotes:

# Many Values to Multiple Variables
x,y,z ='Orange', 'Banana', 'Chery'

print(z)

# One Value to Multiple Variables

m = n =z ="Hiyar"

print(m)
print(z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.


fruits=['apple','banana','chery']

# similary to javaScript destructuring

a , b , c =fruits

# we can use more than one argumant inside print function;

print(a,b,c)


"""
Global Variable:

Same as in JavaScript, variables are defined outside of a block (whic is usually function) is defined as global.

Variable defined inside a fuction is known local.
However,we can create a variable as global inside function with `global` keyword.

"""

def foo():

   # global x ='lovely'
   # #You can't assign a value to a global variable in the same line where you declare it as global.
    global x
    global y

    x='lovely'
    y ='ugly'

foo()
print(x)






















