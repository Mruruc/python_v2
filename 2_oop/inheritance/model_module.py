from abc import ABC, abstractmethod


class ElectronicDevice(ABC):
    def __init__(self, IMEI, manufacturer, price):
        self.IMEI = IMEI
        self.manufacturer = manufacturer
        self.price = price

    @abstractmethod
    def sellingPrice(self):
        pass


class Phone(ElectronicDevice):
    def __init__(self, IMEI, manufacturer, price, isSupport5G):
        super().__init__(IMEI, manufacturer, price)
        self.isSupport5G = isSupport5G

    def sellingPrice(self):
        return self.price * 1.3 if self.isSupport5G else self.price * 1.1

    def __str__(self):
        return f"{self.IMEI}, {self.manufacturer}, {self.price}, {self.isSupport5G}"


class Tablet(ElectronicDevice):
    def __init__(self, IMEI, manufacturer, price, isMakePhoneCall):
        super().__init__(IMEI, manufacturer, price)
        self.isMakePhoneCall = isMakePhoneCall

    def sellingPrice(self):
        return self.price * 1.2 if self.isMakePhoneCall else self.price * 1.1

    def __str__(self):
        return f"{self.IMEI}, {self.manufacturer}, {self.price}, {self.isMakePhoneCall}"
