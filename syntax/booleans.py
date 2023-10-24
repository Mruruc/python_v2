
a = 12
b = 1

if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

print(bool("Something"))
print(bool(5))
print(bool(1))

# falsy value:
print(bool(0))
print(bool(""))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))

print("======================")
# isinstance()
print(isinstance(12, int))
print(isinstance("str" , str))