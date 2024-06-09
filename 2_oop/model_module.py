class Customer:

    def __init__(self, customerId, firstName, lastName):
        self.customerId = customerId
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return f"customerId:{self.customerId},\n firstName:{self.firstName},\n lastName:{self.lastName}"
