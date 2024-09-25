

# method overloading,method overriding __init__ (constructor),__str__(string representation of an object) using Father and son concept


class father():

    def ___init__(self,name,height,weight,age):

        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def __str__(self):

        print(self.name)

    def relation(self):

        print("father")

class son(father):

# overrided the relation from the parent
    def relation(self):

        print("Son")        





    



