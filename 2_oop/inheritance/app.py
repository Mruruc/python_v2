from model_module import Phone, Tablet

phone = Phone("1234567890", "XYZ Corp", 1000, False)
print(phone)

sellingPrice = phone.sellingPrice()
print("Selling Price For Phone:", phone.price, sellingPrice)

tablet = Tablet("5454564555", "Apple", 500, True)
print(tablet)

sellingPriceTablet = tablet.sellingPrice()
print("Selling Price For Tablet: ", tablet.price, sellingPriceTablet)
