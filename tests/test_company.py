import unittest

from models.company import Company

class CompanyTest(unittest.TestCase):
    def test_good(self):
        c = Company(100, 90)
        self.assertEqual(c.profit, 10)

