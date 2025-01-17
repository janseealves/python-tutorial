from abc import ABC, abstractmethod # ------> Abstração 

class MenuItem(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = round(price, 4)
    
    def __str__(self):
        return f'{self._name.ljust(10)} | {str(self._price).ljust(10)}'
    
    @abstractmethod # ------> Abstração
    def applyDiscount(self): 
        pass