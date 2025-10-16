# keys() returns a list of all the keys in the dictionary.
# values() returns a list of all the values in the dictionary.
import datetime

jane_data = dict(first_name="John",
                 last_name="Doe",
                 date_of_birth=datetime.date(1998, 6, 9),
                 email="jane@doe"
                 )

# list_of_keys = jane_data.keys()
# list_of_values = jane_data.values()
# print(list_of_keys)
# print(list_of_values)

# items() returns each item in a dictionary, as tuples in a list.
# print(jane_data.items())

# update() update the dictionary with the items from the given argument. if key does not exist will be created.
# The argument must be a dictionary, or an iterable object with key:value pairs
# jane_data.update({"phone": "+4656565655656"})
# print(jane_data)


# pop() removes the item with given key, returns value of given key.
# popitem() last item removed returns removed key and value as tuple.
# clear() empties the dictionary()

# print(jane_data.pop("email"))
# print(jane_data.popitem())
# print(jane_data)

# Looping through a dictionary

# for key, value in jane_data.items():  # [('first_name', 'John'), ('last_name', 'Doe'), ('date_of_birth', datetime.date(1998, 6, 9)), ('email', 'jane@doe')]
#     print(key, value)
