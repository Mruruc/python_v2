"""
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops

"""

# if statement
a = 1000
b = 100
if a < b:
    print("a is less than b")
elif a <= b:
    print("a is less or equal to b")
else:
    print("a is greater than b")

# conditional expression or inline if

if a > b: print("short hand if ")

age = 18
status = "teenager" if age < 21 else "adult"
print(status)

# && => and, || => or , not => !=
