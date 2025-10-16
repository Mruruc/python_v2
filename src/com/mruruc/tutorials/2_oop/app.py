from model_module import Customer
from customer_service import CustomerService

customer1 = Customer(1, "John", "Doe")
service = CustomerService()

service.save_customer(customer1)
service.save_customer(Customer(2, "Jane", "Doe"))

customers = service.get_all_customers()

# print(customers)

for customer in customers:
    print(customer)
