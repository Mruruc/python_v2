import json


class Customer:
    def __init__(self, customer_id, first_name, last_name):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        return json.dumps({
            "customerId": self.customer_id,
            "firstName": self.first_name,
            "lastName": self.last_name
        })

    @staticmethod
    def from_json(json_obj):
        customer_dict = json.loads(json_obj)
        return Customer(
            customer_dict["customerId"],
            customer_dict["firstName"],
            customer_dict["lastName"]
        )

    def __str__(self):
        return (
            f"customerId:{self.customer_id},\n"
            f"firstName:{self.first_name},\n"
            f"lastName:{self.last_name}"
        )
