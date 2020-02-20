import unittest
from infrastructure.repository import RepositoryFile
from exceptii.erori import RepoError
from domain.entitati import Produs


class TestRepo(unittest.TestCase):
    
    def setUp(self):
    #Pentru fiecare test creez niste entitati si le adaug in repository
    
        self.repo = RepositoryFile('./fisier_test.txt',Produs)
        
        self.produs1 = Produs(1,'asda',20)
        self.produs2 = Produs(0,'',20)
        self.produs3 = Produs(11,'asda',1)
        self.produs4 = Produs(110,'asdas',22)
        self.produs5 = Produs(-1,'asda',20)
        self.produs6 = Produs(12,'asda',20)
        self.produs7 = Produs(11,'asda',-1)
        self.produs8 = Produs(13,'asdas',22)
        
        self.repo.adauga_entitate(self.produs1)
        self.repo.adauga_entitate(self.produs2)
        self.repo.adauga_entitate(self.produs3)
        self.repo.adauga_entitate(self.produs4)
        
    def tearDown(self):
    #Golesc continutul fisierului test dupa fiecare test
        fisier = open('./fisier_test.txt','w')
        fisier.seek(0)
        fisier.truncate()
        fisier.close()
        
    def test_get_all(self):
        
        self.assertEqual(self.repo.get_all(),[self.produs1,self.produs2,self.produs3,self.produs4])
        
    def test_cauta_entitate(self):
        
        self.assertEqual(self.repo.cauta_entitate(self.produs1), 0)
        self.assertEqual(self.repo.cauta_entitate(self.produs4), 3)
        self.assertEqual(self.repo.cauta_entitate(self.produs3), 2)
        self.assertEqual(self.repo.cauta_entitate(self.produs5), -1)
        
    def test_adauga_entitate(self):
        
        with self.assertRaises(RepoError):
            self.repo.adauga_entitate(self.produs7)
            self.repo.adauga_entitate(self.produs8)

        self.repo.adauga_entitate(self.produs6)
        self.assertEqual(self.repo.get_all(), [self.produs1,self.produs2,self.produs3,self.produs4,self.produs6])
        
    def test_sterge_entitate(self):
        
        with self.assertRaises(RepoError):
            self.repo.sterge_entitate(self.produs8)
            
        self.repo.sterge_entitate(self.produs2)
        self.assertEqual(self.repo.get_all(), [self.produs1,self.produs3,self.produs4])
        
if __name__=='__main__':
    unittest.main()
