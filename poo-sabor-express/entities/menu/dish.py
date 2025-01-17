from entities.menu.menu_item import MenuItem

class Dish(MenuItem): # -------> Herança
    def __init__(self, name, price, discription):
        super().__init__(name, price)
        self._discription = discription

    def __str__(self):
        return super().__str__() + f' | {self._discription}'
    
    def applyDiscount(self): #----> Polimorfismo
            self._price -= (self._price * 0.08) # Desconto de 8%