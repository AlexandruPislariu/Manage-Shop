
from exceptii.erori import ValidError,RepoError
class Console(object):
    
    
    def __init__(self, srvProdus):
        self.__srvProdus = srvProdus
        self.__comenzi = {
        'add':self.__ui_adauga_produs,
        'delete':self.__ui_sterge_produs,
        'filter':self.__ui_filtrare_produse,
        'undo':self.__ui_undo}
       
        self.__filtre = ['denumire','pret']
        print(self.__filtre)
    
   
    def __ui_adauga_produs(self,parametrii):
    #Functia comunica cu utilizatorul pentru a adauga un produs
        if len(parametrii)!=3 : #id,denumire,pret
            raise ValueError("Numar incorect de date introduse")
        
        id = parametrii[0]
        denumire = parametrii[1]
        pret = parametrii[2]
        
        self.__srvProdus.adauga_produs(id,denumire,pret)
        
    def __ui_sterge_produs(self,parametrii):
    #Functia comunica cu utilizatorul pentru a sterge un produs ce contine in id o anumita cifra
    
        if len(parametrii)!=1: #cifra
            raise ValueError("Numar incorect de date introduse")
        
        cifra = int(parametrii[0])
        
        self.__srvProdus.sterge_produs(cifra)
        
    def __ui_filtrare_produse(self,parametrii):
    #Functia comunica cu utilizatorul pentru a filtra lista produselor
    
        if len(parametrii)!=2 and len(parametrii)!=1: #pret
            raise ValueError("Numar incorect de date introduse")
        
        if len(parametrii)==1:
            try:
                pret = int(parametrii[0])
                self.__filtre = ['pret']
                rezultat = self.__srvProdus.filtrare_produse([],pret)
                
                print("Filtre: pret")
                #produsele filtrate
                for element in rezultat:
                    print(element)
                        
            except ValueError:
                rezultat = self.__srvProdus.filtrare_produse(parametrii[0],-1)
                
                print("Filtre: denumire")
            #produsele filtrate
                for element in rezultat:
                    print(element)
                        
            
        if len(parametrii)==2:#denumire si pret
            denumire = parametrii[0]
            pret = parametrii[1]
            rezultat = self.__srvProdus.filtrare_produse(denumire,pret)
            
            print("Filtre: denumire si pret")
        #produsele filtrate
            for element in rezultat:
                print(element)
        
    def __ui_undo(self,parametrii):
        
        if len(parametrii)!=0:
            raise ValueError("Numar incorect de date introduse")
        
        self.__srvProdus.undo()
        
    def run(self):
    #Functie principala de rulare a interfetei cu utilizatorul
    
        while True:
            comanda = input("Introduceti comanda dorita!")
            
            if comanda is None:
                print("Comanda invalida!")
                
            if comanda == 'exit':
                print("Aplicatia a fost inchisa cu succes!")
                break
            
            comanda = comanda.split(' ')
            nume_comanda = comanda[0]
            parametrii = comanda[1:]
            
            if nume_comanda in self.__comenzi.keys(): #exista comanda
                try:
                    self.__comenzi[nume_comanda](parametrii)#rulez functionalitatea
                except ValueError as ve:
                    print("UI error: \n" + str(ve))
                except ValidError as valide:
                    print("Valid error: \n" + str(valide))
                except RepoError as re:
                    print("Repo error: \n" + str(re))
                    
            else:
                print("Comanda invalida!")


