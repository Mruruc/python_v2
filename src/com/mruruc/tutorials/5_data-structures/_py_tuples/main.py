# Tuples are immutable, meaning they cannot be changed after creation
# Tuple items are ordered, unchangeable, and allow duplicate values.

client = (1, 'John', 'Doe')
print(type(client))
print("========================")
print(client[0])
print(client[1])
print(client[2])
print("=====================")
for field in client:
    print(field)

# len()
print("======== Length of tuple =============")
print(len(client))

# tuple() constructor
print("======== Tuple constructor =============")
client2 = tuple((2, 'Jane', 'Doe'))
print(client2)
print(type(client2))

# Unpacking
print("======== Unpacking =============")
id, first_name, last_name = client
print(id)
print(first_name)
print(last_name)
# You can use * to collect remaining values
print("======== Unpacking with * =============")
id, *names = client
print(id)
print(names)
# names is now a list containing the remaining values
print(type(names))

# Single item tuple
print("======== Single item tuple =============")
single_item_tuple = (1,)
print(single_item_tuple)
print(type(single_item_tuple))
# Without the comma, it's just an integer
not_a_tuple = (1)
print(not_a_tuple)


x = 1., .5, .25, .125
print(x)
print(type(x))