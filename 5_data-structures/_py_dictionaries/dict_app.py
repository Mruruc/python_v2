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



