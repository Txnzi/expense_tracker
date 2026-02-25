from database.json_storage import ExpenseStorage
class FinanceService:
    __db: ExpenseStorage

    @property
    def db(self):
        return self.__db
    
    def __init__(self,db:ExpenseStorage):
        self.__db=db
    
    def leggi(self):
        self.db.apri()
        lista = [{"id": el.id} for el in self.db.file["expenses"]]




        self.db.chiudi()



    def modifica(self):
        ...
    
    def scrivi(self):
        ...
    
    def elimina(self):
        ...

    def leggi_dett(self):
        ...

    



