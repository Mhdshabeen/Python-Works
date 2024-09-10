# create a class of bikes add bikes to a showroom class and list the bikes in showroom

class bike():

    def __init__(self,name,brand,price):

        self.name=name
        self.brand=brand
        self.price=price

    def __str__(self):

        return self.name
    
dominar_instance=bike("dominar","bajaj",120000)
dio_instance=bike("Dio","Honda",90000)
activa_instance=bike("Activa","Honda",90000)
cbr_instance=bike("CBR","Honda",90000)


class showroom():

    def __init__(self,name,place):

        self.name=name
        self.place=place
        self.bikes=[]

    def add_bikes(self,bike):

        self.bikes.append(bike)

    def list_bikes(self):

        for i in self.bikes:

            print(i)

showroom_instance=showroom("Amana","Mannarkad")

showroom_instance.add_bikes(dio_instance)
showroom_instance.add_bikes(activa_instance)

showroom_instance.list_bikes()