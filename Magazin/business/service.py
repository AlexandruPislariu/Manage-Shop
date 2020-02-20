from domain.entitati import Produs
from exceptii.erori import RepoError
import copy
class ServiceProdus(object):
    
    
    def __init__(self, repoProdus, validProdus):
        self.__repoProdus = repoProdus
        self.__validProdus = validProdus
        self.__lista_undo = []
        
    def adauga_produs(self,id,denumire,pret):
        
        produs = Produs(id,denumire,pret)
        
        if self.__validProdus.validare_produs(produs): #validez
            self.__repoProdus.adauga_entitate(produs)
            
            
    def sterge_produs(self,cifra):
    #sterge toate produsele care contin in id cifra transmisa ca parametru
    
        produse = self.__repoProdus.get_all()
        self.__lista_undo.append(copy.deepcopy(produse))#copie prentru undo
        
        for produs in produse:
            
            id_produs = produs.get_id()
            eliminat = False #presupunem ca nu trebuie eliminat
            
        #Verific daca id_ul contine cifra
            while id_produs>0:
                if id_produs%10 == cifra:#am gasit cifra
                    eliminat = True#marcam ca trebuie eliminat
                    
                id_produs = id_produs//10
                
            if eliminat==True:#daca trebuie eliminat
                self.__repoProdus.sterge_entitate(produs)
    

    def filtrare_produse(self,denumire,pret):
    #Functia filtreaza produsele in functie de denumire si pret
        produse = self.__repoProdus.get_all()
        
        if len(denumire)==0: #filtrare doar dupa pret
            produse = sorted(produse,key = lambda x: x.get_pret())
            return produse

        if pret == -1: #filtrare doar dupa denumire
            produse = sorted(produse,key = lambda x: x.get_denumire())
            return produse
        
        if pret!=-1 and len(denumire)>0:
            produse = sorted(produse,key = lambda x: (x.get_denumire(),x.get_pret()))
            return produse

    def undo(self):
        
        if len(self.__lista_undo)==0:
            raise RepoError("Lista este vida sau nu a avut loc o operatie de stergere")
    
        last = self.__lista_undo.pop()
    
        self.__repoProdus.undo(last)
        
        return last