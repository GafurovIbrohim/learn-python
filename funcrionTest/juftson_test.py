import unittest
from juftsonlar import selectjuftsonlar

class Testjuftsonlar(unittest.TestCase):
    def testjuft(self):
        newsonlar=[1,2,3,4,5,6,7,8]
        check=selectjuftsonlar(newsonlar)
        for son in check:
            self.assertTrue(son%2==0,True)
unittest.main()