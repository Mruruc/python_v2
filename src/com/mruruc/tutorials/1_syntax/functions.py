# In Python a function is defined using the def keyword:
# parameters live inside functions (this is their natural environment)
# arguments exist outside functions, and are carriers of values passed to corresponding parameters.

def say_hello(name):
    print("Hello", name)


say_hello("John")


def foo(first_name: str, last_name: str, age: int):
    print(first_name, last_name, age)


# calling a function using named arguments
# keyword argument passing
foo(first_name="John", age=222, last_name="Doe")


def bar(**kwargs):
    print(kwargs["firstName"], kwargs["lastName"])


bar(firstName="John", age=222, lastName="Doe")


def default_arg(num=1):
    return num * num
