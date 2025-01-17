from entities.restaurant import Restaurant
from entities.menu.dish import Dish
from entities.menu.drink import Drink

restaurantGourmet = Restaurant('Gourmet', 'Alta Gastronomia')

# Ao alterar o estado o interpretador do Python criou uma diretório que armazena os arquivos em bitcode.
# poo-sabor-express\entities\__pycache__\restaurant.cpython-313.pyc

drinkBeer = Drink('Skol', 5.00, 'Grande')
dishBread = Dish('Pão', 2.00, 'O melhor pão da cidade.')

drinkBeer.applyDiscount()
dishBread.applyDiscount()

restaurantGourmet.addOnMenu(drinkBeer)
restaurantGourmet.addOnMenu(dishBread)

def main():
    restaurantGourmet.showMenu

if __name__ == '__main__':
    main() 