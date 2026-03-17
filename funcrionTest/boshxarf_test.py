# Test

import unittest 
from boshharf import matntuzat

class Testboshharf(unittest.TestCase):
    
    def testboshhariftek(self):
        royxat=['kdjffewf ejfhjwefhf','jehfhfewhf yyued']
        royxat2=['Kdjffewf Ejfhjwefhf','Jehfhfewhf Yyued']
        newmatn=matntuzat(royxat)
        self.assertEqual(newmatn,royxat2)

unittest.main()
