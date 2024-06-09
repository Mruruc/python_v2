class CustomerService:
    def __init__(self):
        self.customers = []

    def saveCustomer(self, customer):
        self.customers.append(customer)

    def getAllCustomers(self):
        return self.customers.copy()
