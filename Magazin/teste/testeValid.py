import unittest
from validari.validation import ValidProdus
from exceptii.erori import ValidError
from domain.entitati import Produs

class TestValid(unittest.TestCase):
#In aceasta clasa testez funtia de validare a unui produs
    def setUp(self):
    #Pregatesc niste date pentru fiecare test
    
        self.valid = ValidProdus()
        self.produs1 = Produs(-1,'asda',20)
        self.produs2 = Produs(0,'',20)
        self.produs3 = Produs(11,'asda',-1)
        self.produs4 = Produs(11,'asdas',22)
        
    def tearDown(self):
        pass

    def test_validare_produs(self):
        
        with self.assertRaises(ValidError):
            self.valid.validare_produs(self.produs1)
            self.valid.validare_produs(self.produs2)
            self.valid.validare_produs(self.produs3)
            
        self.assertEqual(self.valid.validare_produs(self.produs4), True)
        
if __name__=='__main__':
    unittest.main()
