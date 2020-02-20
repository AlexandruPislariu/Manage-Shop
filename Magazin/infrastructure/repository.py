from exceptii.erori import RepoError
class RepositoryFile(object):
    
    
    def __init__(self, filename, entity):
        self.__filename = filename
        self.__entity = entity
        self.__lista_entitati = []
        self.__read_all_from_file()
        
        
    def __read_all_from_file(self):
    #Functia citeste continutul unui fisier si adauga entitatile gasite in memorie
        fisier = open(self.__filename,'r')
        
        content = fisier.read()
        content = content.split('\n')
        
        for line in content:
            if line.strip()=='': #linie libera
                continue
            
            entitate = self.__entity.read_entity(line)#creez o entitate din linie
            self.adauga_entitate(entitate)
           
        fisier.close()
         
    def __write_all_in_file(self):
    #Functia adaga lista entitatilor din memorie intr-un fisier
        fisier = open(self.__filename,'w')
        
    #Curat continutul fisierului
        fisier.seek(0)
        fisier.truncate()
        
    #Preiau lista entitatilor
        entitati = self.get_all()
        for element in entitati:
            fisier.write(self.__entity.write_entity(element))
            fisier.write('\n')
            
        fisier.close()
    
    def get_all(self):
        return self.__lista_entitati
    
    def cauta_entitate(self,entitate):
    #Functia cauta o entitate in lista,daca se afla retunreaza indexul, altfel -1
    
        entitati = self.get_all()
        for element in entitati:
            if int(element.get_id()) == int(entitate.get_id()):
                return entitati.index(element)
            
        return -1
    
    def adauga_entitate(self,entitate):
    #Functia adauga o entitate atat in lista din memorie cat si in fisier
        
        index = self.cauta_entitate(entitate)
        if index!=-1: #se afla deja in lista o entitate cu acest id
            raise RepoError("Se afla deja in lista")
        
        self.__lista_entitati.append(entitate)#adaug in lista din memorie
        self.__write_all_in_file()#adaug in fisier
        
    def sterge_entitate(self,entitate):
    #Functia sterge o entitate atat din memorie cat si din fisier
        index = self.cauta_entitate(entitate)
        
        if index == -1: #nu se afla o entitate
            raise RepoError("Nu se afla in lista")
        
        del self.__lista_entitati[index]#modific in memorie
        self.__write_all_in_file()#modific in fisier
        
    def undo(self, lista):
    #Functia reface ultima operatie de stergere
    
    #Modific in memorie
        self.__lista_entitati = []
        for element in lista:
            self.__lista_entitati.append(element)
        
    #Modific in fisier
        self.__write_all_in_file()


