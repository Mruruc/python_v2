# Python does not have syntax for multi line comments.

# Variable: Variables are containers for storing data values.
# whenever we need this value that stored in memory we call this value by variable.

# In Python Variable do not need to be declared with data type(int,String,etc.).
# Even after assigning a value to it, we can change the type.
# It s because Python is Dynamic language.which means the type of variable determine in RUN TIME.

intType = 56
print(intType)

StringType = "Waflo"
print(StringType)

intType = True
print(intType)

print("=======================================================================")
# Casting
# If we want to specify the type of variable we can use casting:

x = str("This is a String.")
y = int(3.6)
z = float(5.6)
m = bool(False)
print(x)
print(y)
print(z)
print(m)

print("=======================================================================")

# Get the Type
# we can learn the type of variable with type() function:
print(type(5))
print(type("This type is String"))
print("=======================================================================")

# Naming Variable:
# for naming convention,for multiple word Variable there are several techniques:

# 1)Camel Case:
# first word of first letter start lowercase Second Word Start Uppercase (Most Common one):
myVariable = "Waflo"

# 2)Pascal Case:
# Each word start Uppercase:
MyVariable = "Waflo"

# 3)Snake Case
# Each word Separated with underscore:
my_Variable = "Waflo"

print("=======================================================================")
# Many Values to Multiple Variables In One Line:
x, y, z = 1, 5, 6
print(x)
print(z)
print(y)

# One Value to Multiple Variables in one line:
x = y = z = 21
print(x)
print(y)
print(z)
print("=======================================================================")
# Unpack a Collection:
# If you have a collection of values in a list,tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("=======================================================================")

# Global Variables:
# The Variables are created outside of function are called Global variable.
# Global Variable are used in anywhere of file.
# Local Variable are belong to their Scope, and They can use just in their scope.

y="Global varibale"
def myFunction():
    global x
    x='This is a local varibale with global keyword we made it global.'
    print(x)
    print(y)
    print("Love!")

print(x)
myFunction()
