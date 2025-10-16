# capitalize() => if the first character inside the string is a letter, it will be converted to upper-case;
# all remaining letters from the string will be converted to lower-case.

# print("aBCd".capitalize())

# center(width, fillchar) => returns a new string which is padded with the specified character (fillchar)
# to make the string centered in a string of length width. If fillchar is not specified, it defaults to a space character.

# print("abc".center(10))
# print("abc".center(10, '*'))

# endswith(suffix, start, end) => returns True if the string ends with the specified suffix,
# otherwise returns False. You can also specify the start and end index to search within a substring.

# print("hello.py".endswith(".py"))
# print("hello.py".endswith("y"))
# print("hello.py".endswith("o", 0, 5))

# startswith(prefix, start, end) => returns True if the string starts with the specified prefix,
# otherwise returns False. You can also specify the start and end index to search within a substring.

# print("hello.py".startswith("he"))
# print("hello.py".startswith("h"))
# print("hello.py".startswith("e", 1, 5))

# find(substring, start, end) => returns the lowest index of the substring if it is found in the string.
# If the substring is not found, it returns -1. You can also specify the start and end index to search within a substring.

# rfind(substring, start, end) => same as find() but it start the search from the end of the string (right of string).

# print("python programming".find("pro"))

# isalnum() checks if the string contains only digits or alphabetical characters (letters),
# and returns True or False according to the result.

# print('lambda'.isalnum())
# print('30'.isalnum())
# print('@'.isalnum())

# isalpha() checks if the string contains only alphabetical characters (letters),
# print('lambda'.isalpha())
# print('30'.isalpha())
# print('@'.isalpha())

# isdigit() checks if the string contains only digits,

# print('lambda'.isdigit())
# print('30'.isdigit())
# print('@'.isdigit())


# join(iterable) => takes all items in an iterable and joins them into one string.
# A string must be specified as the separator.

# print('-'.join(['2024', '06', '25']))
# print("".join([1, 2, 3]))  # TypeError: sequence item 0: expected str instance, int found

# lower() => converts all uppercase characters in a string into lowercase characters and returns it.
# print("HELLO".lower())

# upper() => converts all lowercase characters in a string into uppercase characters and returns it.
# print("hello".upper())

# lstrip() => removes all leading whitespace characters from the string and returns it.
# leading(leading means starting ) whitespace characters are spaces, tabs, and newlines.

# print("   hello   ".lstrip())
# print("ww.hellowww".lstrip("w"))
# print("xyxzyhelloxyzz".lstrip("xyz"))

# rstrip() => removes all trailing whitespace characters from the string and returns it.
# trailing(trailing means ending ) whitespace characters are spaces, tabs, and newlines.
# print("   hello   ".rstrip())
# print("ww.hellowww".rstrip("w"))
# print("xyxzyhelloxyzz".rstrip("xyz"))

# strip() => removes all leading and trailing whitespace characters from the string and returns it.
# leading(leading means starting ) and trailing(trailing means ending ) whitespace characters are spaces, tabs, and newlines.
# print("   hello   ".strip())
# print("ww.hellowww".strip("w"))
# print("xyxzyhelloxyzz".strip("xyz"))

# replace(old, new, count) => returns a copy of the string where all occurrences of a substring (old)
# are replaced with another substring (new). If the optional argument count is given,
# only the first count occurrences are replaced.

# print("hello world".replace("o", "0"))
# print("hello world".replace("o", "0", 1))

# split(sep, maxsplit) => splits the string at the specified separator (sep) and returns a list of substrings.
# If the separator is not specified, any whitespace (space, newline etc.) string is a separator.
# If the optional argument maxsplit is given, the string is split at no more than maxsplit times
# (if maxsplit is -1, then there is no limit on the number of splits).

# print("hello world".split())
# print("hello,world,python".split(","))
# print("hello world python".split(" ", 1))


