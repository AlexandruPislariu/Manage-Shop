import unittest
from infrastructure.repository import RepositoryFile
from validari.validation import ValidProdus
from business.service import ServiceProdus
from exceptii.erori import ValidError,RepoError
from domain.entitati import Produs

class TestService(unittest.TestCase):
    
    def setUp(self):
    #Functia pregateste date pentru fiecare test
    
        self.repo = RepositoryFile('./fisier_test.txt',Produs)
        self.valid = ValidProdus()
        self.service = ServiceProdus(self.repo, self.valid)
        
        self.produs1 = Produs(1,'asda',20)
        self.produs2 = Produs(0,'ddadd',20)
        self.produs3 = Produs(11,'asda',1)
        self.produs4 = Produs(110,'asdas',22)
        self.produs5 = Produs(14,'asda',20)
        self.produs6 = Produs(12,'asda',20)
        self.produs7 = Produs(15,'asda',11)
        self.produs8 = Produs(13,'asdas',22)
        
        self.repo.adauga_entitate(self.produs1)
        self.repo.adauga_entitate(self.produs2)
        self.repo.adauga_entitate(self.produs3)
        self.repo.adauga_entitate(self.produs4)
        self.repo.adauga_entitate(self.produs5)
        self.repo.adauga_entitate(self.produs6)
        self.repo.adauga_entitate(self.produs7)
        self.repo.adauga_entitate(self.produs8)
        
        
    def tearDown(self):
    #Se executa dupa fiecare test
    #Curat fisierul de test
        fisier = open('./fisier_test.txt','w')
        fisier.seek(0)
        fisier.truncate()
        fisier.close()
        
    def test_sterge_produs(self):
        
        self.service.sterge_produs(0)
        self.assertEqual(self.repo.get_all(), [self.produs1,self.produs2,self.produs3,self.produs5,self.produs6,self.produs7,self.produs8])

    def test_filtare_produse(self):
        
        rezultat = self.service.filtrare_produse([], 1)
        
        produse_filtrate = rezultat
        self.assertEqual(produse_filtrate[0].get_id(),self.produs3.get_id())
        self.assertEqual(produse_filtrate[1].get_id(),self.produs7.get_id())
        self.assertEqual(produse_filtrate[2].get_id(),self.produs1.get_id())
        
        

    def test_undo(self):
        
        self.service.sterge_produs(0)
        
        lista = self.service.undo()
        self.assertEqual(lista[0].get_id(), self.produs1.get_id())
        self.assertEqual(lista[1].get_id(), self.produs2.get_id())
        self.assertEqual(lista[2].get_id(), self.produs3.get_id())
        self.assertEqual(lista[3].get_id(), self.produs4.get_id())
        self.assertEqual(lista[4].get_id(), self.produs5.get_id())
        
        with self.assertRaises(RepoError):
            self.service.undo()
            
if __name__=='__main__':
    unittest.main()