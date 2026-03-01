from database.json_storage import ExpenseStorage
from models.expense import Expense
class FinanceService:
    __db: ExpenseStorage
    
    @property
    def db(self):
        return self.__db
    
    def __init__(self,db:ExpenseStorage):
        self.__db=db
        
    def crea_spesa(self):
        new_spesa= {
            "id" : self.db.expenses[-1].id + 1,
            "value" : [input(f"inserisci valore {i} " for i in range(1,3))],
            "catgoryname" : input("è una spesa di alimentari o videogiochi? "),
            "data" : input("inserisci data di acquisto")
            
        }
        if new_spesa["catgoryname"].strip().lower() == "alimentari":
            new_spesa["catgoryname"]= 1
        elif new_spesa["catgoryname"].strip().lower() == "videogiochi":
            new_spesa["catgoryname"]= 2
        else:
            raise ValueError("sei un coglione!")
        return new_spesa
    
    
    def leggi(self):
        self.db.apri()
        lista = [{"id": el.id} for el in self.db.file["expenses"]]




        self.db.chiudi()



    def modifica(self, valori : list[int], categoria : int, id : int):
        self.db.apri()
        for spese in self.db.file["expenses"]:
            if id == spese.id:
                spese.value= valori
                for categorie in self.db.file["categories"]:
                    if categoria == categorie.id:
                        spese.category= categorie
                        self.db.chiudi()
                        return True
        self.db.chiudi()
        return False
    
    
    def scrivi(self):
        self.db.apri()
        new_spesa= self.crea_spesa()
        for categorie in self.db.file["categories"]:
            if new_spesa["categoryname"] == categorie.id:
                new_spesa["categoryname"]= categorie
                crea= Expense(new_spesa["id"], new_spesa["value"], new_spesa["categoryname"], new_spesa["data"])
                self.db.file["expenses"].append(crea)
        self.db.chiudi()
    
    
    def elimina(self):
        ...

    def leggi_dett(self):
        ...

    



