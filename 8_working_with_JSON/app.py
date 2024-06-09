# Python has a built-in package called json, which can be used to work with JSON data.
import json

from model_module import Customer

# json.loads()

john_info_json = '{ "name":"John", "age":30, "city":"New York"}'
print(type(john_info_json))  # <class '4_str'>

john_info_dict = json.loads(john_info_json)  # json.JSONEncoder()
print(john_info_dict)
print(type(john_info_dict))


print("==========================================")
# custom object serialization and deserialization
customer = Customer(1, "John", "Doe")

customer_json = customer.to_json()
print(customer_json)
print(customer.from_json(customer_json))



