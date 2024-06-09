import json


class Customer:
    def __init__(self, customerId, firstName, lastName):
        self.customerId = customerId
        self.firstName = firstName
        self.lastName = lastName

    def to_json(self):
        return json.dumps({
            "customerId": self.customerId,
            "firstName": self.firstName,
            "lastName": self.lastName
        })

    @staticmethod
    def from_json(json_obj):
        customer_dict = json.loads(json_obj)
        return Customer(customer_dict["customerId"], customer_dict["firstName"], customer_dict["firstName"])

    def __str__(self):
        return f"customerId:{self.customerId},\n firstName:{self.firstName},\n lastName:{self.lastName}"
