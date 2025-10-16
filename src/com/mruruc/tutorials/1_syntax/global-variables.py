"""
Global Variable:
Same as in JavaScript, variables are defined outside a block (which is usually function) is defined as global.
Variable defined inside a function is known local.
However,we can create a variable as global inside function with `global` keyword.

"""
# global variable example:

globalVar = "Global Variable"


def foo():
    print(globalVar)

foo()

# local variable

def bar():
    localVar = "Local Variable"
    global localToGlobal
    localToGlobal = "Local, as well as Global variable"
    # global localToGlobal # SyntaxError: name 'localToGlobal' is assigned to before global declaration
    print(localVar)

bar()

print(localToGlobal)



