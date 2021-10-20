import regexfinder
import unittest

class test(unittest.TestCase):
    def regex_test(self):
        self.assertEqual(regexfinder.word_or_number('Ala ma 1 kota oraz psów20 ponadto 50 chomików'), {'words':['Ala', 'ma', 'kota', 'oraz', 'psów', 'ponadto', 'chomików'], 'numbers': ['1', '20', '50']})

if __name__ == '__main__':
    unittest.main()