# A set is a collection which is
#       unordered,
#       unchangeable -> we cannot change the items after the set has been created.,
#       do not allow duplicate values
#       and unindexed ->  cannot be referred to by index or key.

# set items are unchangeable, but you can remove items and add new items.

set_ds = {"apple", "banana", "cherry"}

# print(type(set_ds)) # <class 'set'>

print(set_ds)

# looping through set

for set_item in set_ds:
    print(set_item)

print(dir(set_ds))