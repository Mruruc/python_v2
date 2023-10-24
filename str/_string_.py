# You can assign a multiline string to a variable by using three quotes:

poem="""

Deear ahhhhh, dearrrrr Python
Python Dearrrrrrrrrrrrr


Just Testing Multiline String.

     """


print(poem)



# Like many other popular programming languages,
# strings in Python are arrays of bytes representing unicode characters.

"""
However, Python does not have a character data type,
a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""

a ='Python'
print(a[0],a[1],a[2],a[3])


# Since String are array we can loop through them

for char in "Miskooo":
    print(char)



# String Length

print(len("Come back Please"))



# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"

if 'best' in txt:
   print(True)


# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

print("best" not in txt)


























