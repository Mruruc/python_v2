# Python Strings

- Strings are **immutable sequences** in Python.

---

## `capitalize()`

- Converts the first character of the string to uppercase (if it is a letter) and the rest to lowercase.

```python
print("aBCd".capitalize())  # Output: 'Abcd'
```

---

## `center(width, fillchar)`

- Returns a new string padded with the specified character to make it centered in a string of length `width`.
- If `fillchar` is not specified, it defaults to a space.

```python
print("abc".center(10))      # Output: '   abc    '
print("abc".center(10, '*')) # Output: '***abc****'
```

---

## `endswith(suffix, start, end)`

- Returns `True` if the string ends with the specified suffix, else `False`.
- `start` and `end` can limit the search to a substring.

```python
print("hello.py".endswith(".py"))  # True
print("hello.py".endswith("y"))    # True
print("hello.py".endswith("o", 0, 5)) # True
```

---

## `startswith(prefix, start, end)`

- Returns `True` if the string starts with the specified prefix, else `False`.
- `start` and `end` can limit the search to a substring.

```python
print("hello.py".startswith("he"))  # True
print("hello.py".startswith("h"))   # True
print("hello.py".startswith("e", 1, 5)) # True
```

---

## `find(substring, start, end)` and `rfind(substring, start, end)`

- `find()` returns the lowest index of the substring, or `-1` if not found.
- `rfind()` searches from the end of the string.

```python
print("python programming".find("pro"))  # Output: 7
```

---

## `isalnum()`, `isalpha()`, `isdigit()`

- `isalnum()` → True if string contains only letters or digits.
- `isalpha()` → True if string contains only letters.
- `isdigit()` → True if string contains only digits.

```python
print('lambda'.isalnum())  # True
print('30'.isalnum())      # True
print('@'.isalnum())       # False

print('lambda'.isalpha())  # True
print('30'.isalpha())      # False
print('@'.isalpha())       # False

print('lambda'.isdigit())  # False
print('30'.isdigit())      # True
print('@'.isdigit())       # False
```

---

## `join(iterable)`

- Joins all items in an iterable into a single string using the string as a separator.

```python
print('-'.join(['2024', '06', '25']))  # Output: '2024-06-25'
# print("".join([1, 2, 3]))  # TypeError
```

---

## `lower()` and `upper()`

- `lower()` → Converts all characters to lowercase.
- `upper()` → Converts all characters to uppercase.

```python
print("HELLO".lower())  # 'hello'
print("hello".upper())  # 'HELLO'
```

---

## `lstrip()`, `rstrip()`, `strip()`

- `lstrip()` → Removes leading whitespace (or specified characters).
- `rstrip()` → Removes trailing whitespace (or specified characters).
- `strip()` → Removes leading and trailing whitespace (or specified characters).

```python
print("   hello   ".lstrip())  # 'hello   '
print("ww.hellowww".lstrip("w")) # '.hellowww'
print("xyxzyhelloxyzz".lstrip("xyz")) # 'hello...'

print("   hello   ".rstrip())  # '   hello'
print("ww.hellowww".rstrip("w")) # 'ww.hello'
print("xyxzyhelloxyzz".rstrip("xyz")) # 'xyxzyhello'

print("   hello   ".strip())  # 'hello'
print("ww.hellowww".strip("w")) # '.hello'
print("xyxzyhelloxyzz".strip("xyz")) # 'hello'
```

---

## `replace(old, new, count)`

- Returns a copy of the string with all occurrences of `old` replaced by `new`.
- `count` limits the number of replacements.

```python
print("hello world".replace("o", "0"))   # 'hell0 w0rld'
print("hello world".replace("o", "0", 1)) # 'hell0 world'
```

---

## `split(sep, maxsplit)`

- Splits the string at the separator `sep` and returns a list of substrings.
- If `sep` is not specified, splits on whitespace.
- `maxsplit` limits the number of splits.

```python
print("hello world".split())           # ['hello', 'world']
print("hello,world,python".split(",")) # ['hello', 'world', 'python']
print("hello world python".split(" ", 1)) # ['hello', 'world python']
```
