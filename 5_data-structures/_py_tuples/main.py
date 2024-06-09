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
