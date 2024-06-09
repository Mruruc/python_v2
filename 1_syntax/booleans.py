a = 12
b = 1

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Something"))
print(bool(5))
print(bool(1))

# falsy value:
print("===============Falsy values =======================")
print(bool(0))
print(bool(""))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))

print("======================")
# isinstance()
print(isinstance(12, int))
print(isinstance("4_str", str))
