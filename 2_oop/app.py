from model_module import Customer
from customer_service import CustomerService

customer1 = Customer(1, "John", "Doe")
service = CustomerService()

service.saveCustomer(customer1)
service.saveCustomer(Customer(2,"Jane","Doe"))

customers = service.getAllCustomers()

# print(customers)

for customer in customers:
    print(customer)
