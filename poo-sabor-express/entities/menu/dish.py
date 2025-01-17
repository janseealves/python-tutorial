from entities.menu.menu_item import MenuItem

class Dish(MenuItem): # -------> Herança
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self._description = description

    def __str__(self):
        return super().__str__() + f' | {self._description}'
    
    def applyDiscount(self): #----> Polimorfismo
            self._price -= (self._price * 0.08) # Desconto de 8%