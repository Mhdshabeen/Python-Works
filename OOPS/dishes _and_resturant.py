# resturant
# library

class dish():

    def __init__(self,name,category,type,price):
        self.name=name
        self.category=category
        self.type=type
        self.price=price

    def __str__(self):

        return f"[{self.name},{self.type}]"

dish_instance1=dish("chicken curry","curry","non-veg",120) 
dish_instance2=dish("veg kuruma","curry","veg",100) 
dish_instance3=dish("chicken 65","gravy","non-veg",160) 
dish_instance4=dish("chicken biriyan","Rice","non-veg",110) 
dish_instance5=dish("veg biriyani","rice","veg",90) 


class resturant():

    def __init__(self,name,place):
        self.name=name
        self.place=place
        self.dishes=[]

    def __str__(self):
            
        return f"{self.name},{self.place}"
    
    def add_dishes(self,dish):

        self.dishes.append(dish)

    def list_dishes(self):

        for i in self.dishes:

            print(i)

resturant_instance1=resturant("chillies","mannarkad")

resturant_instance12=resturant("Noora","Pathiripala")

# print(resturant_instance12)

resturant_instance1.add_dishes(dish_instance1)
resturant_instance1.add_dishes(dish_instance2)
resturant_instance1.add_dishes(dish_instance3)

resturant_instance12.add_dishes(dish_instance4)
resturant_instance12.add_dishes(dish_instance5)


# resturant_instance1.list_dishes()

resturant_instance12.list_dishes()



