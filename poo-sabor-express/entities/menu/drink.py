from entities.menu.menu_item import MenuItem

class Drink(MenuItem): # -------> Herança 
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self._size = size

    def __str__(self):
        return super().__str__() + f' | {self._size}'
    
    def applyDiscount(self): #----> Polimorfismo
        self._price -= (self._price * 0.05) # Desconto de 5%