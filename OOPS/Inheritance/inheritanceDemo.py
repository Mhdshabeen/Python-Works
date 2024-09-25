class vehicle:

    name:str

    brand:str

    def __init__(self,name,brand):

        self.name=name

        self.brand=brand

    def start(self):

        print(self.name,"Start vehicle method")

    def accelarate(self):

        print(self.name,"Vehicle accelarate method")


class swift(vehicle):

    def __init__(self, name, brand):
        super().__init__(name, brand)
    

swift_instance=swift("Swift","maruthi")

swift_instance.start()


