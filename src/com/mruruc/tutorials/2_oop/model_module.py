class Customer:

    def __init__(self, customer_id, first_name, last_name):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name

    def get_customer_id(self):
        return self.__customer_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def __str__(self):
        return f"customerId:{self.__customer_id},\n firstName:{self.__first_name},\n lastName:{self.__last_name}"


## Data Classes in Python 3.7+
from dataclasses import dataclass


@dataclass
class CustomerDataClass:
    __customer_id: int
    __first_name: str
    __last_name: str


# customer = CustomerDataClass(1, "John", "Doe")
# print(customer)
# customer.__first_name = "Jane"
# print(customer)

# customer = Customer(1, "John", "Doe")
# customer.__full_name = "Jane Doe"
#
# print(customer.__dict__.keys())
