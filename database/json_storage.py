import json
from models.expense import Expense
from models.category import Category

class ExpenseStorage:
    file : dict[str,int | list[int] | str]
    __path : str
    
    
    @property
    def path(self):
        return self.__path

    def __init__(self, file : None, path : str):
        self.file = None
        self.__path = path
    
    
    def apri(self):
        tmp = {
            "expenses" : [],
            "category" : []
              }
        with open(self.path, "r") as F:
            appoggio= json.load(F)
            for el in appoggio["expenses"]:
                tmp["expenses"].append(Expense(el["id"],el["value"],el["categoryId"],el["data"]))
            for el in appoggio["categories"]:
                tmp["category"].append(Category(el["id"],el["name"]))
                
    
    def chiudi(self):
        pass