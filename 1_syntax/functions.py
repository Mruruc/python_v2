# In Python a function is defined using the def keyword:

def sayHello(name):
    print("Hello", name)


sayHello("John")


def foo(firstName, lastName, age):
    print(firstName, lastName, age)


foo(firstName="John", age=222, lastName="Doe")


def bar(**kwargs):
    print(kwargs["firstName"], kwargs["lastName"])


bar(firstName="John", age=222, lastName="Doe")


def defaultArg(num=1):
    return num * num


print(defaultArg())
print(defaultArg(10))
