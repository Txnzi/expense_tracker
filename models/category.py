class Category:
    __id: int
    name: str

    @property
    def id(self):
        return self.__id


    def __init__(self, id: int, name: str):
        self.__id = id
        self.name = name