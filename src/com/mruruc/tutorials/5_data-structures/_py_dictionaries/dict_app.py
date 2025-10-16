# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
import datetime

john_data = {
    "first_name": "John",
    "last_name": "Doe",
    "date_of_birth": datetime.date(1998, 6, 9),
    "email": "john@doe"
}

print(john_data["first_name"])

jane_data = dict(first_name="John",
                 last_name="Doe",
                 date_of_birth=datetime.date(1998, 6, 9),
                 email="jane@doe"
                 )

print(type(jane_data))
jane_data["email"] = "new@email"
print(jane_data.get("email"))


"""
The dictionary key:value pairs are enclosed in curly braces {}.
- each key must be unique.
- a key must be immutable (string, number or tuple) not a list or set.
- values can be of any data type and can be duplicated.
"""

# looping through dictionary
print("==================================")
for key in jane_data:
    print(f"{key}: {jane_data[key]}")

print("==================================")
print(jane_data.items())
for key, value in jane_data.items():
    print(f"{key}: {value}")

