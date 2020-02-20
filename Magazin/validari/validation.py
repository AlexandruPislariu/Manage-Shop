from exceptii.erori import ValidError
class ValidProdus():
    def validare_produs(self,produs):
    #Functia valideaza atributele unui produs
    #validez id-ul
        id = produs.get_id()
        try:
            id = int(id)
            
            if id<0:
                raise ValidError("ID invalid")
            
            
        except ValueError :
            raise ValidError("ID invalid")
        
    #validez denumire
        if produs.get_denumire() is None:
            raise ValidError("Produs invalid")
        
    #validez pretul
        pret = produs.get_pret()
        try:
            pret = int(pret)
            
            if pret<0:
                raise ValidError("Pret invalid")
            
        except ValueError:
            raise ValidError("Pret invalid")
        
        return True


