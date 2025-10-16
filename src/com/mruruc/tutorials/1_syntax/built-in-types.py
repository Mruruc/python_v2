# There are about 15 built-in types in Python:

# 1. Numeric types: int, float, complex
a: int = 10  # int
b: float = 3.14  # float
c: complex = 1 + 2j  # complex

print(type(a), type(b), type(c))

# 2. String type: str
s: str = "Hello, World!"  # str
print(type(s))

# 3. Sequence types: list, tuple, range
lst: list = [1, 2, 3, 4, 5]  # list
tup: tuple = (1, 2, 3)  # tuple
rng: range = range(5)  # range

print(type(lst), type(tup), type(rng))

# 4. Mapping type: dict
map1: dict = {"key1": "value1", "key2": "value2"}  # dict
# map2:dict = dict(key1="value1", key2="value2")

print(type(map1))
# print(type(map2))

# 5. Set types: set, frozenset
set1: set = {1, 2, 3}  # set
set2: frozenset = frozenset([1, 2, 3])  # frozenset

print(type(set1), type(set2))

# 6. Boolean type: bool
flag: bool = True  # bool
print(type(flag))

# 7. Binary types: bytes, bytearray, memoryview
b1: bytes = b"Hello"  # bytes
b2: bytearray = bytearray(b"Hello")  # bytearray
b3: memoryview = memoryview(b"Hello")  # memoryview
print(type(b1), type(b2), type(b3))

# 8. None type: NoneType
n: None = None  # NoneType
print(type(n))