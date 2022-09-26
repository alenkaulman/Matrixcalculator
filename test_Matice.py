import unittest
from matice import Matice


# vytvoření testovací třídy, která dědí ze třídy TestCase
class TestMatic(unittest.TestCase):

    def pocitej(self,funkce,testMatrix1,testMatrix2,vysledek):
        #funkce a matice
        test = Matice(funkce,testMatrix1,testMatrix2)
        test.provedOperaci()
        #porovnani vypoctu s predpokladanym vysledkem
        stejne = (test.vystup==vysledek).all()
        return stejne

    def test_sum(self):
        #matice zadani
        testMatrix1 = [[1, 2], [1, 3]]
        testMatrix2 = [[4, 1], [2, 1]]
        #funkce
        funkce = "sum"
        #vysledek
        vysledek = [[5, 3], [3, 4]]
        #vyhodnoceni, zda jsou stejne
        self.assertEqual(self.pocitej(funkce,testMatrix1,testMatrix2,vysledek), True)


    def test_multiply(self):
        #matice zadani
        testMatrix1 = [[3, 6], [4, 1]]
        testMatrix2 = [[2, 5], [7, 2]]
        #funkce
        funkce = "multiply"
        #vysledek
        vysledek = [[48, 27], [15, 22]]
        #vyhodnoceni, zda jsou stejne
        self.assertEqual(self.pocitej(funkce,testMatrix1,testMatrix2,vysledek), True)

