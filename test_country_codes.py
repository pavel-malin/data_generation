""""Tests functions about the city to perform work. (country_codes.py)"""
import unittest

from country_codes import get_country_code

class TestCoutryCodes(unittest.TestCase):

    def test_country_code(self):
        name = get_country_code('Andorra')
        self.assertEqual(name, 'ad')


unittest.main()
