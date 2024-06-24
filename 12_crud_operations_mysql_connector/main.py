from model.model_module import Customer
from repository.client_repository import ClientRepository

# customer = Customer(1, "John", "Doe")
# customer2 = Customer(1, "Jane", "Doe")
#
repository = ClientRepository()

# result = repository.save_client(customer2)
#
# print(result)

# print(client_list)

# for client in repository.get_all_client():
#     print(client)

#print(repository.update_client(1,"Bob","Bobee"))
print(repository.get_client_by_id(1))

# print(repository.delete_client(2))
