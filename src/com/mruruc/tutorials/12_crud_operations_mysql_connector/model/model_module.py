class Customer:

    def __init__(self, customer_id, first_name, last_name):
        self.customerId = customer_id
        self.firstName = first_name
        self.lastName = last_name

    def __str__(self):
        return f"customerId:{self.customerId},firstName:{self.firstName},lastName:{self.lastName}"
