from database.json_storage import ExpenseStorage
from models.expense import Expense
class FinanceService:
    __db: ExpenseStorage
    id_liberati : None
    
    @property
    def db(self):
        return self.__db
    
    def __init__(self,db:ExpenseStorage, id_liberati : None):
        self.__db=db
        self.id_liberati= [int] | None
        
    def crea_spesa(self):
        if self.id_liberati is not None:
            nuovo_id= self.id_liberati[0]
            self.id_liberati= self.id_liberati[1:]
        else:
            nuovo_id= self.db.expenses[-1].id + 1
        new_spesa= {
            "id" : nuovo_id,
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
        
        return lista



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
    
    
    def elimina(self, id : int):
        self.db.apri()
        for spesa in self.db.file["expenses"]:
            if id == spesa.id:
                self.id_liberati.append(id)
                del spesa
        self.db.chiudi()


    def leggi_dett(self, id : int):
        self.db.apri()
        for spesa in self.db.file["expenses"]:
            if spesa.id == id:
                spesa_dettagliata={"id" : id, "value" : spesa.value, "categoryId" : spesa.category, "data" : spesa.data}
                return spesa_dettagliata
        return False

    



