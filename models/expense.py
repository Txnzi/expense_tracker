from category import Category

class Expense: 
    
    __id : int
    value : list[int]
    __category : Category
    data : str
    
    
    @property
    def id(self):
        return self.__id
    
    @property
    def category(self):
        return self.__category
    
    @property.setter
    def category(self, new_category : Category):
        if isinstance(new_category, Category):
            self.__category = new_category
            
    
    def __init__(self, id : int, value : list[int], category : Category, data : str) :
        self.__id = id
        self.value = value
        self.__category = category
        self.data : str