from abc import ABC, abstractmethod



class Fruits(ABC):
    @abstractmethod
    def quantity(self):
        raise NotImplementedError
    
class Banana(Fruits):
    def quantity(self):
        print("This is quantity")


class Apple(Fruits):
    def quantity(self):
        print("this is Apple")


bn: Fruits = Banana()
bn.quantity()