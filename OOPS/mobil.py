# __init__() used to initialize instance variables
#  and __str__() for string representation

class mobile():

    def __init__(self,name,brand,ram,rom,camera,price):

        self.name=name
        self.brand=brand
        self.ram=ram
        self.rom=rom
        self.camera=camera
        self.price=price

    def __str__(self):

        return self.name
    
mobile_instance=mobile("Iphone 16","Apple","128 GB","8 GB","105 MP",50000)
mobile_instance2=mobile("Iphone 15","Apple","256 GB","16 GB","105 MP",80000)

print(mobile_instance)