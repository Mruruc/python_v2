# A 3_lambda function is a small anonymous function
# a lamda function can take any number of arguments, but can only have one express

"""
Syntax:
     3_lambda arguments : expression
Note: Use 3_lambda functions when an anonymous function is required for a short period of time.
"""

# sum = lambda x, y: x + y
#
# result = sum(1, 10)
#
#
# # print(result)
# def foo(m):
#     return lambda a: m + a
#
#
# bar = foo(12)
#
# print(bar(10))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_nums_iterator = filter(lambda n: n % 2 == 0, nums)

for num in even_nums_iterator:
    print(num)
