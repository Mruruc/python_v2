from model_module import Phone, Tablet

phone1 = Phone("1234567890", "XYZ Corp", 1000, False)
# print(phone1)

# selling_price_phone1 = phone1.selling_price()
# print("Selling Price For Phone:", phone1.price, selling_price_phone1)

phone2 = Phone("1234567890", "XYT Corp", 999, False)

# print(phone1 == phone2)  # True
# print(phone1 is phone2)  # False

tablet = Tablet("5454564555", "Apple", 501, True)
tablet2 = Tablet("5454564555", "Apple", 500, True)
# print(tablet == tablet2)  # False
# print(tablet is tablet2)  # False
# print(tablet)

print(tablet.__hash__()) # 
print(tablet2.__hash__())

# selling_price_tablet = tablet.selling_price()
# print("Selling Price For Tablet: ", tablet.price, selling_price_tablet)
