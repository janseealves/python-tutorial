from entities.review import Review
from entities.menu.menu_item import MenuItem

class Restaurant: 
    restaurants = []

    #Construtor: 
    def __init__(self, name, category):
        self._name = name.title() #self = this (Java)
        self._category = category.upper()
        self._isActive = False # O _ protege o atributo de modificações diretas
        self._reviews = []
        self._menu = []
        Restaurant.restaurants.append(self) #Após criar o objeto Restaurant, o mesmo é add na lista de restaurants.

    # = toString() (Java) 
    def __str__(self): 
        return f'{self._name} | {self._category}'
    
    # __init__ e __str__ são métodos especiais, ou "dunder methods", incorporados na linguagem.
    
    @classmethod
    def printRestaurants(cls): 
        print(f'{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Media'.ljust(20)} | {'Status'}')
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {str(restaurant.avgReview).ljust(20)} | {restaurant.isActive}')

    @property #modifica a forma que o atributo é lido (Encapsulamento)
    def isActive(self):
        return f'☑' if self._isActive else '☐' #https://coolsymbol.com/
    
    def setIsActive(self):
        self._isActive = not self._isActive

    def setReview(self, client, rating):
        review = Review(client, rating)
        if(0 <= review._rating <= 5):
            self._reviews.append(review)
        else:
            return 'Error: Nota inválida!' 

    @property
    def avgReview(self):
        if not self._reviews:
            return '-'

        sumRating = sum(review._rating for review in self._reviews)
        average = round(sumRating / len(self._reviews), 1)

        return average

    def addOnMenu(self, item):
        if isinstance(item, MenuItem): # isistance(Objeto, Classe) Retorna True quando o item comparado for uma instância ou derivado da classe comparada.
            self._menu.append(item)
    @property
    def showMenu(self):
        print(f'Cardápio do restaurante {self._name}: \n')
        for i, item in enumerate(self._menu, start=1):
            if hasattr(item, '_discription'): # hasattr(Objeto, Atributo) Returna True quando o item argumento tem o atributo com o nome especificado.
                print(f'{i}. Nome: {item._name.ljust(20)} | Preço: ${str(item._price).ljust(20)} | Descrição: {item._discription}')

            if hasattr(item, '_size'):
                print(f'{i}. Nome: {item._name.ljust(20)} | Preço: ${str(item._price).ljust(20)} | Tamanho: {item._size}')


            