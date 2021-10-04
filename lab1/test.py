from fractions import Fraction
import main
import unittest


class Test_TestSum(unittest.TestCase):
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
        self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        try:
            self.assertEqual(main.sum(2, 'Ala ma kota123'), 2)
        except Exception:
            print(Exception())

    def test_exception(self):
        self.assertRaises(Exception, main.sum, 2, 'Ala ma kota123')
        self.assertRaises(Exception, main.sum, 2, [1,2])
        self.assertRaises(Exception, main.sum, [1,2], {1,2})

    def test_sum_rational_rational(self):
        self.assertEqual(main.sum(Fraction(3,4), Fraction(1,4)), 1)

    def test_sum_rational_string(self):
        self.assertEqual(main.sum(Fraction(12,13), '1'), float(Fraction(25, 13)))

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum(complex(3,2), complex(1,1)), complex(4,3))

    def test_sum_complex_string(self):
        self.assertEqual(main.sum(complex(3,2), '1'), complex(4, 2))

            
if __name__ == '__main__':
    unittest.main()