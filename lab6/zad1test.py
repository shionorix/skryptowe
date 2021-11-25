import unittest
from zad1 import Operacje


class Test_Zad1(unittest.TestCase):
    def setUp(self):
        global op
        op = Operacje()
        
    def test_suma(self):
        self.assertEqual(op.suma(1,2,3), 4) #nie pobiera nic
        self.assertEqual(op.suma(1,2), 5) #pobiera 4
        self.assertEqual(op.suma(1), None) #pobiera 4 i 5

    def test_roznica(self):
        self.assertEqual(op.roznica(2,1), 4) #nie pobiera nic
        self.assertEqual(op.roznica(2), 5) #pobiera 4
        self.assertEqual(op.roznica(), 6) #pobiera 4 i 5

    def test_error(self):
        with self.assertRaises(TypeError):
            op.suma()

    def test_change_defaultArgs(self):
        op['suma']=[1,2]
        self.assertEqual(op.suma(1), None) #pobiera wszystko
        self.assertEqual(op.suma(1, 1), 2) #pobiera 1
        self.assertEqual(op.suma(1, 1, 1), 1) #nic nie pobiera

        op['roznica']=[1,2,3]
        self.assertEqual(op.roznica(), 3) #pobiera 1 i 2
        self.assertEqual(op.roznica(1), 2) #pobiera 1
        self.assertEqual(op.roznica(1, 1), 1) #nic nie pobiera

if __name__ == "__main__":
    unittest.main()