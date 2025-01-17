from entities.restaurant import Restaurant 

restaurantGourmet = Restaurant('Gourmet', 'Alta Gastronomia')

# Ao alterar o estado o interpretador do Python criou uma diretório que armazena os arquivos em bitcode.
# poo-sabor-express\entities\__pycache__\restaurant.cpython-313.pyc

def main():
    Restaurant.printRestaurants()

if __name__ == '__main__':
    main() 