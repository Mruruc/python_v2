import model_module as model

class CustomerService:
    __customers = []

    def __init__(self):
        pass

    def save_customer(self, customer):
        self.__customers.append(customer)

    def get_all_customers(self):
        return self.__customers.copy()


# customer_service = CustomerService()
# customer1 = model.Customer(1, "John", "Doe")
# customer2 = model.Customer(2, "Jane", "Smith")
#
# customer_service.save_customer(customer1)
# customer_service.save_customer(customer2)
#
# all_customers = customer_service.get_all_customers()
# for customer in all_customers:
#     print(customer)


