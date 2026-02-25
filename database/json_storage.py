import json
from ..models.expense import Expense
from ..models.category import Category

class ExpenseStorage:
    file : dict[str, Expense | Category] | None
    __path : str
    
    
    @property
    def path(self):
        return self.__path

    def __init__(self, path : str):
        self.file = None
        self.__path = path
    
    
    def apri(self):
        tmp = {
            "expenses" : [],
            "categories" : []
              }
        with open(self.path, "r") as F:
            appoggio= json.load(F)
            for el in appoggio["expenses"]:
                tmp["expenses"].append(Expense(el["id"],el["value"],el["categoryId"],el["data"]))
            for el in appoggio["categories"]:
                tmp["categories"].append(Category(el["id"],el["name"]))
                
    
    def chiudi(self):
        with open(self.path , "w") as F:
            json.dump(F, self.file)