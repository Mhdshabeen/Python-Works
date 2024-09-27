

# Abstraction
# Hiding the implimentation details
from abc import ABC,abstractmethod

class car(ABC):

    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def accelarate(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass


class swift(car):

    def start(self):
        print("Swift start method")

    def accelarate(self):
        print("Swift accelarate method")

    def stop(self):
        print("Swift stop method")

car_swift=swift()

car_swift.stop()
