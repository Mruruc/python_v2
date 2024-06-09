import math
from cusom_exceptions import Custom_Exception1, Custom_Exception2

num = input("Please Enter a number:")

try:
    num = int(num)  # value error
    print(math.pow(num, 2))  # type error
except TypeError:
    print("Enter Number !")
except ValueError:
    print("I said Enter Number....")


def validate_input(input):
    if input:
        return True
    raise Exception("Input can not be None!")


print(validate_input("Hello"))
print(validate_input(12))

# raise Custom_Exception1("Default Message")

# raise Custom_Exception2("Default Message", "Extra Info")
