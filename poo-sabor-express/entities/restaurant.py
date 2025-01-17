from entities.review import Review

class Restaurant: 
    restaurants = []

    #Construtor: 
    def __init__(self, name, category):
        self._name = name.title() #self = this (Java)
        self._category = category.upper()
        self._isActive = False # O _ protege o atributo de modificações diretas
        self.__reviews = []
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
            self.__reviews.append(review)
        else:
            return 'Error: Nota inválida!' 

    @property
    def avgReview(self):
        if not self.__reviews:
            return '-'

        sumRating = sum(review._rating for review in self.__reviews)
        average = round(sumRating / len(self.__reviews), 1)

        return average