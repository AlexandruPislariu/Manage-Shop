class Produs():
    
    def __init__(self,id,denumire,pret):
        self.__id = id
        self.__denumire = denumire
        self.__pret = pret

    def get_id(self):
        return self.__id


    def get_denumire(self):
        return self.__denumire


    def get_pret(self):
        return self.__pret


    def set_denumire(self, value):
        self.__denumire = value


    def set_pret(self, value):
        self.__pret = value

    @classmethod
    def read_entity(cls,line):
    #Functia transforma o linie intr-o entitate produs
        line = line.split(' ')
        id = int(line[0])
        denumire = line[1]
        pret = int(line[2])
        
        return Produs(id,denumire,pret)
    
    @classmethod
    def write_entity(cls,produs):
    #Functia converteste un produs intr-un string pentru a putea fi scris in fisier
        return str(str(produs.get_id()) + " " + produs.get_denumire() + " " + str(produs.get_pret()))

    def __str__(self):
        
        return str(str(self.get_id()) + " " + self.get_denumire() + " " + str(self.get_pret()))
        