from abc import ABC, abstractmethod


class ElectronicDevice(ABC):
    def __init__(self, IMEI, manufacturer, price):
        self.IMEI = IMEI
        self.manufacturer = manufacturer
        self.price = price
    def __eq__(self, value):
        return isinstance(value, ElectronicDevice) and \
               self.IMEI == value.IMEI and \
               self.manufacturer == value.manufacturer and \
               self.price == value.price

    def __hash__(self):
        return hash((self.IMEI, self.manufacturer, self.price))

    @abstractmethod
    def selling_price(self):
        pass


class Phone(ElectronicDevice):
    def __init__(self, IMEI, manufacturer, price, is_support_5G):
        super().__init__(IMEI, manufacturer, price)
        self.is_support_5G = is_support_5G

    def selling_price(self):
        return self.price * 1.3 if self.is_support_5G else self.price * 1.1
    
    def __eq__(self, value):
        return super().__eq__(value) and \
              isinstance(value, Phone) and \
              self.is_support_5G == value.is_support_5G

    def __hash__(self):
        return hash((self.IMEI, self.manufacturer, self.price, self.is_support_5G))

    def __str__(self):
        return f"{self.IMEI}, {self.manufacturer}, {self.price}, {self.is_support_5G}"


class Tablet(ElectronicDevice):
    def __init__(self, IMEI, manufacturer, price, is_make_phone_call):
        super().__init__(IMEI, manufacturer, price)
        self.is_make_phone_call = is_make_phone_call

    def selling_price(self):
        return self.price * 1.2 if self.is_make_phone_call else self.price * 1.1
    
    def __eq__(self, other):
        return super().__eq__(other) and \
               isinstance(other, Tablet) and \
               self.is_make_phone_call == other.is_make_phone_call

    def __hash__(self):
        return hash((self.IMEI, self.manufacturer, self.price, self.is_make_phone_call))

    def __str__(self):
        return f"{self.IMEI}, {self.manufacturer}, {self.price}, {self.is_make_phone_call}"
