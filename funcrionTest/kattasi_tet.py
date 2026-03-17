import unittest
from Kattasi import getmax

class Testmax(unittest.TestCase):
    def testmaximum(self):
        son1=int(input('Son kiriting : '))
        son2=int(input('Son kiriting : '))
        son3=int(input('Son kiriting : '))
        maxson=getmax(son1,son2,son3)
        self.assertAlmostEqual(maxson,max(son1,son2,son3))
unittest.main()