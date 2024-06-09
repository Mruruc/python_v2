# A 3_lambda function is a small anonymous function
# a lamda function can take any number of arguments, but can only have one express

"""
Syntax:
     3_lambda arguments : expression
Note: Use 3_lambda functions when an anonymous function is required for a short period of time.
"""

sum = lambda x, y: x + y

result = sum(1, 10)


# print(result)
def foo(m):
    return lambda a: m + a


bar = foo(12)

print(bar(10))
